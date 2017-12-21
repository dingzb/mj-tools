# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(257, 182)
        self.formLayoutWidget = QtGui.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 241, 111))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.iPLabel = QtGui.QLabel(self.formLayoutWidget)
        self.iPLabel.setObjectName(_fromUtf8("iPLabel"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.iPLabel)
        self.iPLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.iPLineEdit.setObjectName(_fromUtf8("iPLineEdit"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.iPLineEdit)
        self.pORTLabel = QtGui.QLabel(self.formLayoutWidget)
        self.pORTLabel.setObjectName(_fromUtf8("pORTLabel"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.pORTLabel)
        self.pORTLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.pORTLineEdit.setObjectName(_fromUtf8("pORTLineEdit"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.pORTLineEdit)
        self.uSERNAMELabel = QtGui.QLabel(self.formLayoutWidget)
        self.uSERNAMELabel.setObjectName(_fromUtf8("uSERNAMELabel"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.uSERNAMELabel)
        self.uSERNAMELineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.uSERNAMELineEdit.setObjectName(_fromUtf8("uSERNAMELineEdit"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.uSERNAMELineEdit)
        self.pASSWORDLabel = QtGui.QLabel(self.formLayoutWidget)
        self.pASSWORDLabel.setObjectName(_fromUtf8("pASSWORDLabel"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.pASSWORDLabel)
        self.pASSWORDLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.pASSWORDLineEdit.setObjectName(_fromUtf8("pASSWORDLineEdit"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.pASSWORDLineEdit)
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 130, 241, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.iPLabel.setText(_translate("Dialog", "IP", None))
        self.pORTLabel.setText(_translate("Dialog", "PORT", None))
        self.uSERNAMELabel.setText(_translate("Dialog", "USERNAME", None))
        self.pASSWORDLabel.setText(_translate("Dialog", "PASSWORD", None))
        self.pushButton_2.setText(_translate("Dialog", "Save", None))
        self.pushButton.setText(_translate("Dialog", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

