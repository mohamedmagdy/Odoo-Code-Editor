import sys
from PyQt4 import QtGui
from ext import *


class Main(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.filename = ""
        self.setWindowIcon(QtGui.QIcon("icons/icon.png"))
        self.initUI()

    def initUI(self):
        self.text = QtGui.QTextEdit(self)
        self.setCentralWidget(self.text)

        self.initToolbar()
        self.initMenubar()

        # Initialize a statusbar for the window
        self.statusbar = self.statusBar()

        # If the cursor position changes, call the function that displays
        # the line and column number
        self.text.cursorPositionChanged.connect(self.cursorPosition)

        # X and Y coordinates on the screen, width, height
        self.setGeometry(100, 100, 1030, 800)
        self.setWindowTitle("Odoo Code Editor")

    def initToolbar(self):

        # New
        self.newAction = QtGui.QAction(QtGui.QIcon("icons/new.png"), "New", self)
        self.newAction.setStatusTip("Create a new file.")
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.triggered.connect(self.new)

        # Open
        self.openAction = QtGui.QAction(QtGui.QIcon("icons/open.png"), "Open file", self)
        self.openAction.setStatusTip("Open an existing file.")
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.open)

        # Save
        self.saveAction = QtGui.QAction(QtGui.QIcon("icons/save.png"), "Save", self)
        self.saveAction.setShortcut("Save")
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self.save)

        # Action
        self.cutAction = QtGui.QAction(QtGui.QIcon("icons/cut.png"), "Cut", self)
        self.cutAction.setStatusTip("Delete and copy text to clipboard")
        self.cutAction.setShortcut("Ctrl+X")
        self.cutAction.triggered.connect(self.text.cut)

        # Copy
        self.copyAction = QtGui.QAction(QtGui.QIcon("icons/copy.png"), "Copy", self)
        self.copyAction.setStatusTip("Copy text to clipboard")
        self.copyAction.setShortcut("Ctrl+C")
        self.copyAction.triggered.connect(self.text.copy)

        # Paste
        self.pasteAction = QtGui.QAction(QtGui.QIcon("icons/paste.png"), "Paste", self)
        self.pasteAction.setStatusTip("Paste text from clipboard")
        self.pasteAction.setShortcut("Ctrl+V")
        self.pasteAction.triggered.connect(self.text.paste)

        # Undo
        self.undoAction = QtGui.QAction(QtGui.QIcon("icons/undo.png"), "Undo", self)
        self.undoAction.setStatusTip("Undo last action")
        self.undoAction.setShortcut("Ctrl+Z")
        self.undoAction.triggered.connect(self.text.undo)

        # Redo
        self.redoAction = QtGui.QAction(QtGui.QIcon("icons/redo.png"), "Redo", self)
        self.redoAction.setStatusTip("Redo last undone thing")
        self.redoAction.setShortcut("Ctrl+Y")
        self.redoAction.triggered.connect(self.text.redo)

        # Find
        self.findAction = QtGui.QAction(QtGui.QIcon("icons/find.png"), "Find and replace", self)
        self.findAction.setStatusTip("Find and replace words in your document")
        self.findAction.setShortcut("Ctrl+F")
        self.findAction.triggered.connect(find.Find(self).show)

        self.toolbar = self.addToolBar("Options")

        self.toolbar.addAction(self.newAction)
        self.toolbar.addAction(self.openAction)
        self.toolbar.addAction(self.saveAction)
        self.toolbar.addSeparator()

        self.toolbar.addAction(self.cutAction)
        self.toolbar.addAction(self.copyAction)
        self.toolbar.addAction(self.pasteAction)
        self.toolbar.addAction(self.undoAction)
        self.toolbar.addAction(self.redoAction)

        self.toolbar.addSeparator()
        self.toolbar.addAction(self.findAction)

        # Makes the next toolbar appear underneath this one
        self.addToolBarBreak()

    def initMenubar(self):
        menubar = self.menuBar()

        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("View")
        tools = menubar.addMenu("Tools")
        help = menubar.addMenu("Help")

        # File Menu
        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAction)

        # Edit Menu
        edit.addAction(self.undoAction)
        edit.addAction(self.redoAction)
        edit.addAction(self.cutAction)
        edit.addAction(self.copyAction)
        edit.addAction(self.pasteAction)
        edit.addAction(self.findAction)

    def new(self):
        spawn = Main(self)
        spawn.show()

    def open(self):
        # Get filename and get only .py, .xml, .csv files
        self.filename = QtGui.QFileDialog.getOpenFileName(self, "Open File", ".", "*.py *.xml *.csv")

        if self.filename:
            with open(self.filename, "rt") as file:
                self.text.setText(file.read())

    def save(self):
        # Only open dialog if there is no filename yet
        if not self.filename:
            self.filename = QtGui.QFileDialog.getSaveFileName(self, "Save File")

        # We just storethe contents of the test file along with the
        # format in plain text
        with open(self.filename, "wt") as file:
            file.write(self.text.toPlainText())

    def cursorPosition(self):
        cursor = self.text.textCursor()

        # Mortals like 1-indexed things
        line = cursor.blockNumber() + 1
        col = cursor.columnNumber()

        self.statusbar.showMessage("Line: {} | Column: {}".format(line, col))


def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
