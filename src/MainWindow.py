# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'APP2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 711)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(400, 300))
        self.centralwidget.setStyleSheet(_fromUtf8(""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setMargin(3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget_2 = QtGui.QWidget(self.splitter)
        self.widget_2.setMaximumSize(QtCore.QSize(120, 16777215))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.listWidget = QtGui.QListWidget(self.widget_2)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.horizontalLayout_2.addWidget(self.listWidget)
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.splitter_2 = QtGui.QSplitter(self.widget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.widget_3 = QtGui.QWidget(self.splitter_2)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 300))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.formLayout = QtGui.QFormLayout(self.widget_3)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.pushButton = QtGui.QPushButton(self.widget_3)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.pushButton)
        self.pushButton_5 = QtGui.QPushButton(self.widget_3)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.pushButton_5)
        self.pushButton_4 = QtGui.QPushButton(self.widget_3)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.pushButton_4)
        self.pushButton_3 = QtGui.QPushButton(self.widget_3)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.pushButton_3)
        self.pushButton_2 = QtGui.QPushButton(self.widget_3)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.pushButton_2)
        self.textBrowser = QtGui.QTextBrowser(self.splitter_2)
        self.textBrowser.setBaseSize(QtCore.QSize(0, 50))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_4.addWidget(self.splitter_2)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_4.addWidget(self.lineEdit)
        self.horizontalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuConnections = QtGui.QMenu(self.menubar)
        self.menuConnections.setObjectName(_fromUtf8("menuConnections"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.menuConnections.addAction(self.actionNew)
        self.menubar.addAction(self.menuConnections.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton", None))
        self.menuConnections.setTitle(_translate("MainWindow", "Connections", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

