import sys

from PyQt4 import QtGui, QtCore

from qq import Ui_self


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        # self.ui_main_window = Ui_self()
        # self.ui_main_window.setupUi(self)
        # self.ui_main_window.actionNew.triggered.connect(self.__show_conn_window)
        # self.actionNew.triggered.connect(self.__show_conn_window)
        # self.pushButton.clicked.connect(self.__show_conn_window)
        # self.connect(self.actionNew, QtCore.SIGNAL("triggered()"), self.__show_conn_window)
        buton = QtGui.QPushButton(self)
        buton.move(0, 30)
        buton.clicked.connect(self.__show_conn_window)
        ac = QtGui.QAction(self)
        ac.setText("q")
        ac.triggered.connect(self.__show_conn_window)
        menubar = QtGui.QMenuBar(self)
        menubar.setGeometry(QtCore.QRect(0, 0, 798, 23))
        menubar.setObjectName("menubar")
        menu = QtGui.QMenu(self)
        menu.setObjectName("adsf")
        menu.setTitle("aaaaaaa")
        menubar.addMenu(menu)
        menu.addAction(ac)

    def __show_conn_window(self):
        dialog = QtGui.QDialog()
        dialog.resize(300, 200)
        hostname = QtGui.QLineEdit(dialog)
        hostname.move(10, 10)
        dialog.exec_()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    #
    sys.exit(app.exec_())