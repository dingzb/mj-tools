import sys

from PyQt4 import QtGui
from PyQt4.QtCore import QSettings

import Main


def main():
    app = QtGui.QApplication(sys.argv)
    main_window = Main.MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()