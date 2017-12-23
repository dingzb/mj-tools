# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connection.ui'
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

class Ui_ConnWindow(object):
    def setupUi(self, ConnWindow):
        ConnWindow.setObjectName(_fromUtf8("ConnWindow"))
        ConnWindow.setWindowModality(QtCore.Qt.NonModal)
        ConnWindow.resize(400, 100)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConnWindow.sizePolicy().hasHeightForWidth())
        ConnWindow.setSizePolicy(sizePolicy)
        ConnWindow.setMinimumSize(QtCore.QSize(0, 0))
        ConnWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label = QtGui.QLabel(ConnWindow)
        self.label.setGeometry(QtCore.QRect(10, 10, 50, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(ConnWindow)
        self.lineEdit.setGeometry(QtCore.QRect(70, 10, 120, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(ConnWindow)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 10, 120, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_2 = QtGui.QLabel(ConnWindow)
        self.label_2.setGeometry(QtCore.QRect(210, 10, 50, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(ConnWindow)
        self.label_3.setGeometry(QtCore.QRect(210, 40, 50, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(ConnWindow)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 50, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_3 = QtGui.QLineEdit(ConnWindow)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 40, 120, 20))
        self.lineEdit_3.setText(_fromUtf8(""))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(ConnWindow)
        self.lineEdit_4.setGeometry(QtCore.QRect(70, 40, 120, 20))
        self.lineEdit_4.setText(_fromUtf8(""))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.pushButton = QtGui.QPushButton(ConnWindow)
        self.pushButton.setGeometry(QtCore.QRect(315, 70, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(ConnWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 70, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(ConnWindow)
        QtCore.QMetaObject.connectSlotsByName(ConnWindow)

    def retranslateUi(self, ConnWindow):
        ConnWindow.setWindowTitle(_translate("ConnWindow", "Connection", None))
        self.label.setText(_translate("ConnWindow", "HostName", None))
        self.label_2.setText(_translate("ConnWindow", "Port", None))
        self.label_3.setText(_translate("ConnWindow", "Password", None))
        self.label_4.setText(_translate("ConnWindow", "Username", None))
        self.pushButton.setText(_translate("ConnWindow", "Connect", None))
        self.pushButton_2.setText(_translate("ConnWindow", "Save", None))

