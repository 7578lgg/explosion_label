import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from label_demo import Ui_mainWindow



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(widget)
    widget.show()
    app.exec_()