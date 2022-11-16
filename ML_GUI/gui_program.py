from PyQt5 import QtWidgets , uic , QtCore
import pandas as pd
import sys
import table_display
from sklearn.preprocessing import StandardScaler , MinMaxScaler , PowerTransformer , LabelEncoder


class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('uifiles/mainwindow.ui' , self)
        self.item = None
        self.target_value =None
        self.openPushButton = self.findChild(QtWidgets.QPushButton ,"Browse")
        self.columnList = self.findChild(QtWidgets.QListWidget ,"column_list")
        self.target_col = self.findChild(QtWidgets.QLabel, 'target_col')
        self.submitButton = self.findChild(QtWidgets.QPushButton ,"Submit")
        self.tableView = self.findChild(QtWidgets.QTableView, "tableView")
        self.shape = self.findChild(QtWidgets.QLabel, 'shape')
        self.scaler = self.findChild(QtWidgets.QComboBox, 'scaler')
        self.scale_btn = self.findChild(QtWidgets.QPushButton, 'scale_btn')

        self.cat_column = self.findChild(QtWidgets.QComboBox, 'cat_column')
        self.convert_btn = self.findChild(QtWidgets.QPushButton, 'convert_btn')

        self.drop_column = self.findChild(QtWidgets.QComboBox, 'drop_column')
        self.drop_btn = self.findChild(QtWidgets.QPushButton, 'drop_btn')


        self.columnList.clicked.connect(self.target)
        self.openPushButton.clicked.connect(self.openFile)
        self.submitButton.clicked.connect(self.set_target)
        self.scale_btn.clicked.connect(self.scale_value)
        self.convert_btn.clicked.connect(self.con_cat)

        self.drop_btn.clicked.connect(self.dropc)
        self.show()

    def dropc(self):
        x = self.drop_column.currentText()
        print(x)
        if ( x == self.target_value ):
            self.target_value = ""
            self.target_col.setText("")
        self.df = self.df.drop(x , axis=1)

        self.fillDetails()

    def con_cat(self):
        x = self.cat_column.currentText()
        le = LabelEncoder()
        self.df[x] = le.fit_transform(self.df[x])
        self.fillDetails()

    def scale_value(self):
        print(self.target_value)
        if self.target_value ==None:
            print("set Target")
            if self.scaler.currentText() == "StandardScale":
                sc = StandardScaler()
                scaled_features = sc.fit_transform(self.df)
                

            elif self.scaler.currentText() == "MinMaxScale":
                sc = MinMaxScaler()
                scaled_features = sc.fit_transform(self.df)
                

            elif self.scaler.currentText() == "PowerScale":
                sc = PowerTransformer()
                scaled_features = sc.fit_transform(self.df)
                
                
        else:
            x = self.df.drop(self.target_value , axis=1)
            if self.scaler.currentText() == "StandardScale":
                sc = StandardScaler()
                scaled_features = sc.fit_transform(x)
                scaled_df= pd.DataFrame(scaled_features, index=x.index , columns=x.columns)
                scaled_df[self.target_value] = self.df[self.target_value]
                print(scaled_df)
                self.df = scaled_df
                print(scaled_features)
                # return self.df

            elif self.scaler.currentText() == "MinMaxScale":
                sc = MinMaxScaler()
                scaled_features = sc.fit_transform(x)
                scaled_df= pd.DataFrame(scaled_features, index=x.index , columns=x.columns)
                scaled_df[self.target_value] = self.df[self.target_value]
                print(scaled_df)
                self.df = scaled_df
                print(scaled_features)
                

            elif self.scaler.currentText() == "PowerScale":
                sc = PowerTransformer()
                scaled_features = sc.fit_transform(x)
                scaled_df= pd.DataFrame(scaled_features, index=x.index , columns=x.columns)
                scaled_df[self.target_value] = self.df[self.target_value]
                print(scaled_df)
                self.df = scaled_df
                print(scaled_features)
            # print(self.scaler.currentText())
            # print(x)

        self.fillDetails()


    def set_target(self):
        if self.item ==None:
            self.target_col.setText("Not Selected")
        else:
            self.target_value = self.item.text().split(" ")[0]
            self.target_col.setText(self.target_value)

    def target(self):
        self.item = self.columnList.currentItem()
        print(self.item.text())

    def fillDetails(self, flag = 1):
        if flag ==0:
            self.df = pd.read_csv(self.filePath)
            print(self.df.columns)

        for i , j in enumerate(self.df.columns):
            str = f"{j} -------  {self.df[j].dtype}"
            self.columnList.insertItem( i , str)
        # print(self.filePath)
        cat_cal = []
        for i in self.df.columns:
            if (self.df[i].dtype =='object'):
                cat_cal.append(i)
        self.cat_col_list = cat_cal
        print(self.cat_col_list)
        self.fill_combo_box()

    def fill_combo_box(self):

        self.cat_column.clear() 
        self.cat_column.addItems(self.cat_col_list)

        self.drop_column.clear() 
        self.drop_column.addItems(self.df.columns)

        x = table_display.DataFrameModel(self.df)
        print(self.df.shape)
        self.shape.setText(f'Rows : {self.df.shape[0]} , Colunm : {self.df.shape[1]}')
        self.tableView.setModel(x)

    def openFile(self):
        self.filePath , _ = QtWidgets.QFileDialog.getOpenFileName(self ,"Open File", "", "csv(*.csv)")
        # print(self.filePath)
        self.columnList.clear()
        self.fillDetails(0)

    


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    main = UI()
    sys.exit(app.exec_())