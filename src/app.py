import sys

import paramiko
from PyQt4 import QtGui
from PyQt4 import QtCore
from MainWindow import Ui_MainWindow
from new import Ui_Dialog
from SSHConnection import Connection, Connect


def main():
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    mainWindow.move(100, 100)
    sys.exit(app.exec_())


class MainWindow1(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.actionNew.triggered.connect(self.new_connection)

    def connect_dev(self):
        self.statusbar.showMessage("Connecting...")
        self.sshClient = paramiko.SSHClient()
        self.sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.sshClient.connect("192.168.168.23", 22122, "root", "t0d7r19tdr")
        stdin, stdout, stderr = self.sshClient.exec_command("ls /")
        self.statusbar.showMessage("Connected.")
        self.textBrowser.setText(stdout.read())

    def new_connection(self):
        self.newWindow = NewWindow()
        self.newWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        # self.newWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        self.newWindow.show()

class NewWindow(QtGui.QMainWindow, Ui_Dialog):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_Dialog.__init__(self)
        self.setupUi(self)



class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.actionNew.triggered.connect(self.connect_dev)

    def connect_dev(self):
        connection = Connection("192.168.168.23", 22122, "root", "t0d7r19tdr")
        # self.sshClient.connect(self.ip, self.port, self.user, self.password)
        # return self
        connectThread = Connect(connection)
        connectThread.msgSignal.connect(self.set_msg)
        connectThread.start()
        # connection.open(self.set_msg)

    def set_msg(self, msg):
        self.statusBar().showMessage(msg)

if __name__ == '__main__':
    main()
