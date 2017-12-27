# coding=utf-8
import sys
import paramiko
from PyQt4 import QtGui
from PyQt4 import QtCore


class MainWindow(QtGui.QMainWindow):
    __ssh_client = paramiko.SSHClient()

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.__ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.resize(400, 300)
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setText(u'连接')
        self.pushButton.clicked.connect(self.__connect)
        self.move(10, 10)
        self.textBrowser = QtGui.QTextBrowser(self)
        self.textBrowser.resize(300, 200)
        self.textBrowser.move(50, 50)
        self.pushButtonExeCmd = QtGui.QPushButton(self)
        self.pushButtonExeCmd.setText(u'执行')
        self.pushButtonExeCmd.clicked.connect(self.__exe_cmd)
        self.pushButtonExeCmd.move(40, 30)
        self.lineEditCmd = QtGui.QLineEdit(self)
        self.lineEditCmd.move(250, 0)
        self.lineEditCmd.returnPressed.connect(self.__exe_cmd)

    def __connect(self):
        self.connect = Connect(self.__ssh_client)
        self.connect.msg_signal.connect(self.__msg_append)
        self.connect.start()

    def __exe_cmd(self):
        cmd = self.lineEditCmd.text()
        stdin, stdout, stderr = self.__ssh_client.exec_command(str(cmd))
        self.__msg_append(stdout.read())

    def __msg_append(self, msg):
        self.textBrowser.append(msg)


class Connect(QtCore.QThread):
    msg_signal = QtCore.pyqtSignal(str)

    def __init__(self, ssh_client):
        QtCore.QThread.__init__(self)
        self.__ssh_client = ssh_client

    def run(self):
        self.msg_signal.emit('connect')
        self.__ssh_client.connect('192.168.128.150', 22, 'root', '112')


def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
