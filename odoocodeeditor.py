import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt


class Main(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.initUI()

    def initUI(self):
        # X and Y coordinates on the screen, width, height
        self.setGeometry(100, 100, 1030, 800)
        self.setWindowTitle("Odoo Code Editor")

def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
