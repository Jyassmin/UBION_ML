from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, uic, QtCore, QtGui
import sys

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('uifiles/mainwindow_basic.ui', self)
        
        self.label_1 = self.findChild(QtWidgets.QLabel, "label")
        self.button_1 = self.findChild(QtWidgets.QPushButton, "pushButton")
        
        self.button_1.clicked.connect(self.textin)
    
    def textin(self):
        self.label_1.setText("버튼을 클릭 했냐?") # text 입력
        



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    window.show()
    
    sys.exit(app.exec_())