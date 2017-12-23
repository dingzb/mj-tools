from PyQt4.QtGui import *
from B import B


class A(QWidget):
    def __init__(self, parent=None):
        super(A, self).__init__(parent)
        self.resize(400, 300)
        self.setWindowTitle("Class A")
        self.mIP = QLineEdit(self)
        self.mIP.setText("192.168.20.1")
        self.mIP.move(0, 0)
        self.mBtn = QToolButton(self)
        self.mBtn.setText("get IP")
        self.mBtn.move(100, 100)
        self.mBtn.clicked.connect(self.handleGetIPClick)
        self.mBWidget = B()

    def handleGetIPClick(self, *args, **kwargs):
        ipValue = self.mIP.text()
        self.c = B()
        print id(self.c)
        if ipValue:
            self.mBWidget.setIP(ipValue)
            if not self.mBWidget.isVisible():
                self.mBWidget.show()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    a = A()
    a.show()
    app.exec_()