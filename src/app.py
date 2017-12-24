import sys

from PyQt4 import QtGui

from ConnWindow import Ui_ConnWindow
from MainWindow import Ui_MainWindow
from SSHConnection import Connection


class ConnWindow(Ui_ConnWindow):
    def __init__(self):
        Ui_ConnWindow.__init__(self)


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.actionNew.triggered.connect(self.__show_conn_window)

    def __show_conn_window(self):
        self.Form1 = QtGui.QDialog()
        # ui = Dialog1()
        # ui.ss = QtGui.QLineEdit()
        # ui.setupUi(Form1)
        # Form1.show()
        self.Form1.exec_()
        # self.form.show()

    def __connect_dev(self):
        connection = Connection("192.168.128.150", 22, "root", "112")
        connection.open(self.__set_msg)

    def __set_msg(self, msg):
        self.statusBar().showMessage(msg)


def __show_conn_window():
        Form1 = QtGui.QDialog()
        Form1.exec_()

def main():
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()