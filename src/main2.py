# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.resize(600, 400)
        self.setWindowTitle("MJ-TOOLS")

        # toolBar = self.addToolBar("ToolBar")
        # toolBar.setMovable(False)
        # actionDisconnect = QtGui.QAction(QtGui.QIcon("res/application-exit.png"), "Disconnect", self)
        # toolBar.addAction(actionDisconnect)

        # menuBar
        menuBar = self.menuBar()
        menuConnections = menuBar.addMenu("Connections")
        actionNew = menuConnections.addAction("New")
        actionNew.triggered.connect(self.new_connection)

        left = QtGui.QListWidget(self)
        left.addItem("192.168.100.102")
        left.addItem("192.168.100.104")
        left.addItem("192.168.100.106")
        left.addItem("192.168.100.108")
        left.setGeometry(-1, 23, 130, 378)

        left = QtGui.QListWidget(self)
        left.addItem("192.168.100.102")
        left.addItem("192.168.100.104")
        left.addItem("192.168.100.106")
        left.addItem("192.168.100.108")
        left.setGeometry(-1, 23, 130, 377)

        topright = QtGui.QFrame(self)
        topright.setFrameShape(QtGui.QFrame.StyledPanel)

        vsplitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        vsplitter.addWidget(left)
        vsplitter.addWidget(topright)
        self.layout().addWidget(vsplitter)
        # vbox.addWidget(left)

        # self.setLayout(vbox)

    def new_connection(self):
        print("1111")
        self.statusBar().showMessage("new")



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())