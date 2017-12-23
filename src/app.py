import sys

from PyQt4 import QtGui

from ConnWindow import Ui_ConnWindow
from MainWindow import Ui_MainWindow
from SSHConnection import Connection


class ConnWindow(Ui_ConnWindow):
    def __init__(self):
        Ui_ConnWindow.__init__(self)


class MainWindow(Ui_MainWindow):
    def __init__(self, parent):
        Ui_MainWindow.__init__(self)
        self.setupUi(parent)
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

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QMainWindow()
    # mainWindowUI = MainWindow(mainWindow)
    mainWindow.move(100, 100)
    ii = QtGui.QPushButton(mainWindow)
    ii.move(0,0)
    ii.clicked.connect(__show_conn_window)
    mainWindow.show()
    #
    sys.exit(app.exec_())
    # app = QtGui.QApplication(sys.argv)
    # Form = QtGui.QWidget()
    # window = MainWindow()
    # window.setupUi(Form)
    # Form.show()
    # sys.exit(app.exec_())
