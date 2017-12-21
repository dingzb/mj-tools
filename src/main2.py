import sys
from PyQt4 import QtGui

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        menuBar = QtGui.QMenuBar
        menuConnections = QtGui.QMenu()
        menuConnections.setObjectName("Connections")
        actionNew = QtGui.QAction(self)
        actionNew.setObjectName("New")
        menuConnections.addAction(actionNew)
        menuBar.addMenu(menuConnections)
        self.setMenuBar(menuBar)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())