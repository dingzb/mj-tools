import json
import re
from PyQt4 import QtGui, QtCore

from SSHConnection import Connection
from UIConnection import Ui_ConnectionDialog
from UIMainWindow import Ui_MainWindow

FILE_CONNECTIONS = 'recent.json'
FILE_SETTINGS = '.mj-tools.ini'
SETTING_GROUP_CUSTOM = "custom"
SETTING_KEY_SIZE = 'size'
SETTING_KEY_POSITION = 'position'
SETTING_KEY_MAX = 'max'


class MainWindow(Ui_MainWindow, QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        super(QtGui.QMainWindow, self).__init__()
        self.setupUi(self)
        self.actionNew.triggered.connect(self.__show_conn_window)
        self.actionExit.triggered.connect(self.close)

        self.__settings = QtCore.QSettings(FILE_SETTINGS, QtCore.QSettings.IniFormat)
        if self.__read_max():
            self.showMaximized()
        else:
            self.resize(self.__read_size())
            self.move(self.__read_position())

    def __show_conn_window(self):
        connection_dialog = ConnectionDialog(self.__print_msg, self.__set_conn)
        connection_dialog.exec_()

    def __print_msg(self, msg):
        self.browserRecord.append(str(msg))

    def __set_conn(self, conn):
        self.__connect(conn)

    def closeEvent(self, *args, **kwargs):
        self.__write_position(self.pos())
        self.__write_size(self.size())
        self.__write__max(self.isMaximized())
        self.__close_conn()
        QtGui.QMainWindow.closeEvent(self, *args, **kwargs)

    def __connect(self, conn):
        try:
            self.conn = Connection(**conn)
            self.conn.open(self.__print_msg)
        except Exception, e:
            print(str(e))

    def __close_conn(self):
        if hasattr(self, 'conn'):
            self.conn.close()

    def __write_position(self, point):
        self.__settings.beginGroup(QtCore.QString(SETTING_GROUP_CUSTOM))
        self.__settings.setValue(QtCore.QString(SETTING_KEY_POSITION), QtCore.QVariant(point))
        self.__settings.endGroup()

    def __write_size(self, size):
        self.__settings.beginGroup(QtCore.QString(SETTING_GROUP_CUSTOM))
        self.__settings.setValue(QtCore.QString(SETTING_KEY_SIZE), QtCore.QVariant(size))
        self.__settings.endGroup()

    def __write__max(self, is_max):
        self.__settings.beginGroup(QtCore.QString(SETTING_GROUP_CUSTOM))
        self.__settings.setValue(QtCore.QString(SETTING_KEY_MAX), QtCore.QVariant(is_max))
        self.__settings.endGroup()

    def __read_position(self):
        return self.__settings.value(QtCore.QString(SETTING_GROUP_CUSTOM + '/' + SETTING_KEY_POSITION),
                                     QtCore.QVariant(QtCore.QPoint(300, 300))).toPoint()

    def __read_size(self):
        return self.__settings.value(QtCore.QString(SETTING_GROUP_CUSTOM + '/' + SETTING_KEY_SIZE),
                                     QtCore.QVariant(QtCore.QSize(600, 250))).toSize()

    def __read_max(self):
        return self.__settings.value(QtCore.QString(SETTING_GROUP_CUSTOM + '/' + SETTING_KEY_MAX),
                                     QtCore.QVariant(False)).toBool()


class ConnectionDialog(Ui_ConnectionDialog, QtGui.QDialog):
    def __init__(self, set_msg, conn_callbak):
        super(ConnectionDialog, self).__init__()
        super(QtGui.QDialog, self).__init__()
        self.setupUi(self)
        self.buttonConnect.clicked.connect(self.__save_connect)
        self.__set_msg = set_msg
        self.__conn_callbak = conn_callbak
        self.__read()

    def __save(self):
        connection = self.__validate()
        if connection:
            j_rec = [connection]
            rec_file = open(FILE_CONNECTIONS, 'w')
            json.dump(j_rec, rec_file)
            rec_file.close()
            self.close()
            return connection

    def __read(self):
        rec_file = open(FILE_CONNECTIONS, 'r')
        try:
            j_rec = json.load(rec_file)
        except Exception, e:
            j_rec = json.loads('[]')
        rec_file.close()
        j_rec = list(j_rec)
        if len(j_rec) > 0:
            rec = dict(j_rec[0])
            self.editHostname.setText(str(rec.get('hostname')))
            self.editPort.setText(str(rec.get('port')))
            self.editUsername.setText(str(rec.get('username')))
            self.editPassword.setText(str(rec.get('password')))

    def __validate(self):
        hostname = self.editHostname.text()
        port = self.editPort.text()
        username = self.editUsername.text()
        password = self.editPassword.text()
        if not re.match(r'^(?:(?:1[0-9][0-9]\.)|(?:2[0-4][0-9]\.)|(?:25[0-5]\.)|(?:[1-9][0-9]\.)|(?:[0-9]\.)){3}(?:(?:1[0-9][0-9])|(?:2[0-4][0-9])|(?:25[0-5])|(?:[1-9][0-9])|(?:[0-9]))$', hostname):
            return False
        if not re.match(r'\d{2,5}', port):
            return False
        if not re.match(r'.+', username):
            return False
        if not re.match(r'.+', password):
            return False
        return {
            'hostname': str(hostname),
            'port': int(port),
            'username': str(username),
            'password': str(password)
        }

    def __save_connect(self):
        _conn = self.__save()
        if _conn:
            self.__conn_callbak(_conn)


class RecWrite(QtCore.QThread):
    def __init__(self, rec):
        QtCore.QThread.__init__(self)
        self.__rec = rec

    def run(self):
        rec_file = open(FILE_CONNECTIONS, 'w')
        json.dump(self.__rec, rec_file)
        rec_file.close()
