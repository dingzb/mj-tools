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

class Ui_ConnectionDialog(object):
    def setupUi(self, ConnectionDialog):
        ConnectionDialog.setObjectName(_fromUtf8("ConnectionDialog"))
        ConnectionDialog.setWindowModality(QtCore.Qt.NonModal)
        ConnectionDialog.resize(400, 100)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConnectionDialog.sizePolicy().hasHeightForWidth())
        ConnectionDialog.setSizePolicy(sizePolicy)
        ConnectionDialog.setMinimumSize(QtCore.QSize(0, 0))
        ConnectionDialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label = QtGui.QLabel(ConnectionDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 50, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.editHostname = QtGui.QLineEdit(ConnectionDialog)
        self.editHostname.setGeometry(QtCore.QRect(70, 10, 120, 20))
        self.editHostname.setObjectName(_fromUtf8("editHostname"))
        self.editPort = QtGui.QLineEdit(ConnectionDialog)
        self.editPort.setGeometry(QtCore.QRect(270, 10, 120, 20))
        self.editPort.setObjectName(_fromUtf8("editPort"))
        self.label_2 = QtGui.QLabel(ConnectionDialog)
        self.label_2.setGeometry(QtCore.QRect(210, 10, 50, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(ConnectionDialog)
        self.label_3.setGeometry(QtCore.QRect(210, 40, 50, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(ConnectionDialog)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 50, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.editPassword = QtGui.QLineEdit(ConnectionDialog)
        self.editPassword.setGeometry(QtCore.QRect(270, 40, 120, 20))
        self.editPassword.setText(_fromUtf8(""))
        self.editPassword.setObjectName(_fromUtf8("editPassword"))
        self.editUsername = QtGui.QLineEdit(ConnectionDialog)
        self.editUsername.setGeometry(QtCore.QRect(70, 40, 120, 20))
        self.editUsername.setText(_fromUtf8(""))
        self.editUsername.setObjectName(_fromUtf8("editUsername"))
        self.buttonConnect = QtGui.QPushButton(ConnectionDialog)
        self.buttonConnect.setGeometry(QtCore.QRect(315, 70, 75, 23))
        self.buttonConnect.setObjectName(_fromUtf8("buttonConnect"))
        self.buttonSave = QtGui.QPushButton(ConnectionDialog)
        self.buttonSave.setGeometry(QtCore.QRect(230, 70, 75, 23))
        self.buttonSave.setObjectName(_fromUtf8("buttonSave"))

        self.retranslateUi(ConnectionDialog)
        QtCore.QMetaObject.connectSlotsByName(ConnectionDialog)
        ConnectionDialog.setTabOrder(self.editHostname, self.editPort)
        ConnectionDialog.setTabOrder(self.editPort, self.editUsername)
        ConnectionDialog.setTabOrder(self.editUsername, self.editPassword)
        ConnectionDialog.setTabOrder(self.editPassword, self.buttonConnect)

    def retranslateUi(self, ConnectionDialog):
        ConnectionDialog.setWindowTitle(_translate("ConnectionDialog", "Connection", None))
        self.label.setText(_translate("ConnectionDialog", "HostName", None))
        self.label_2.setText(_translate("ConnectionDialog", "Port", None))
        self.label_3.setText(_translate("ConnectionDialog", "Password", None))
        self.label_4.setText(_translate("ConnectionDialog", "Username", None))
        self.buttonConnect.setText(_translate("ConnectionDialog", "Connect", None))
        self.buttonSave.setText(_translate("ConnectionDialog", "Save", None))

