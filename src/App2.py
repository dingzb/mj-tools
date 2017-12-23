import sys
from PyQt4 import QtGui

from src.MainWindow import Ui_MainWindow
from src.qq import Ui_self


class MainWindow(Ui_self):
    def __init__(self):
        Ui_self.__init__(self)
        # QtGui.QMainWindow.__init__(self)
        # self.ui_main_window = Ui_self()
        # self.ui_main_window.setupUi(self)
        # self.ui_main_window.actionNew.triggered.connect(self.__show_conn_window)
        self.actionNew.triggered.connect(self.__show_conn_window)
        # # buton = QtGui.QPushButton(self)
        # # buton.move(0, 0)
        # # buton.clicked.connect(self.__show_conn_window)
        # ac = QtGui.QAction(self)
        # ac.setText("q")
        # ac.triggered.connect(self.__show_conn_window)
        # self.ui_main_window.menubar.addAction(ac)
        # menubar = QtGui.QMenuBar(self)
        # menubar.addAction(ac)

    def __show_conn_window(self):
        dialog = QtGui.QDialog()
        dialog.exec_()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.move(100, 100)
    mainWindow.show()
    #
    sys.exit(app.exec_())