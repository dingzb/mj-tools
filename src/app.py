import sys

import paramiko
from PyQt4 import QtGui
from PyQt4 import QtCore
from main import Ui_MainWindow
from new import Ui_Dialog

def main():
    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    w.resize(450, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
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


if __name__ == '__main__':
    # main()
    app = QtGui.QApplication(sys.argv)
    toolWindow = MainWindow()
    toolWindow.show()
    sys.exit(app.exec_())
