from PyQt4.QtGui import *

class B(QDialog):
    def __init__(self, parent=None):
        super(B, self).__init__(parent)
        self.mIP = QLineEdit(self)
        self.mIP.move(0, 0)
        self.setWindowTitle("Class B")
        self.resize(200, 100)

    def setIP(self, ipValue):
        self.mIP.clear()
        self.mIP.setText(ipValue)