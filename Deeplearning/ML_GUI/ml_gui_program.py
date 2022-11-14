from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, uic, QtCore, QtGui
import sys
import pandas as pd

class UI(QtWidgets.QMainWindow):
    def __init__(self ):
        super(UI, self).__init__()
        uic.loadUi('unicodes/mainwindow.ui' , self)

        # 객체 등록 : 객체 등록기의 (객체명, 클래스명)에 맞게
        self.label_1 = self.findChild(QtWidgets.QLabel , "label")
        self.Browser_btn = self.findChild(QtWidgets.QPushButton , "Browser")
        self.columns = self.findChild(QtWidgets.QListWidget , "column_list") 
        
        # 클릭으로 객체를 사용하고 싶으면 clicked.connect !
        self.Browser_btn.clicked.connect(self.GetCsv) # Browser 버튼 클릭시 GetCsv 함수 실행!


    # 객체 기능을 함수로 정의
    def filldetails(self, flag =1 ): # flag가 1 일 때는 작동하지 않도록
        if flag==0:
            self.df = pd.read_csv(str(self.filePath))
            
    def GetCsv(self): # 클릭했을 때 파일탐색기를 열어 csv를 가져오게함
        self.filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "ubion5", "", "csv(*.csv)") # (csv인 파일의) 파일경로 이름을 get
        print(self.filePath)
        self.columns.clear()
        self.columns.insertItem(0, self.filePath)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    window.show()
    
    sys.exit(app.exec_())