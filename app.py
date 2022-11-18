from PySide2 import QtCore, QtWidgets, QtGui

class SearchWindow(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()

class IndexWindow(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("moyu")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    indexWindow = IndexWindow()
    indexWindow.show()

    app.exec_()