from PyQt5 import QtWidgets, uic, QtCore
import pandas as pd
import sys
import table_display
from sklearn.preprocessing import StandardScaler, MinMaxScaler, PowerTransformer, LabelEncoder
import matplotlib.pyplot as plt

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        # uic.loadUi('uicodes/mainwindow3.ui', self)
        uic.loadUi('uifiles/mainwindow.ui', self)
        self.item = None
        self.target_value = None
        self.openPushButton = self.findChild(QtWidgets.QPushButton,"Browse")
        self.column_list = self.findChild(QtWidgets.QListWidget,"column_list")
        self.target_col = self.findChild(QtWidgets.QLabel, 'target_col')
        self.submitButton = self.findChild(QtWidgets.QPushButton, 'Submit')
        self.shape = self.findChild(QtWidgets.QLabel, 'shape')
        self.scaler = self.findChild(QtWidgets.QComboBox, 'scaler')
        self.scale_botton = self.findChild(QtWidgets.QPushButton, 'scale_btn')

        self.cat_column = self.findChild(QtWidgets.QComboBox, 'cat_column')
        self.convert_btn = self.findChild(QtWidgets.QPushButton, 'convert_btn')

        self.drop_column = self.findChild(QtWidgets.QComboBox, 'drop_column')
        self.drop_btn = self.findChild(QtWidgets.QPushButton, 'drop_btn')

        self.empty_column = self.findChild(QtWidgets.QComboBox, 'empty_column')
        self.fill_mean = self.findChild(QtWidgets.QPushButton, 'fill_mean')
        self.fill_na = self.findChild(QtWidgets.QPushButton, 'fill_na')


        # scatter plot
        self.scatter_x = self.findChild(QtWidgets.QComboBox, 'scatter_x')
        self.scatter_y = self.findChild(QtWidgets.QComboBox, 'scatter_y')
        self.scatter_c = self.findChild(QtWidgets.QComboBox, 'scatter_c')
        self.scatter_mark = self.findChild(QtWidgets.QComboBox, 'scatter_mark')
        self.scatter_vmin = self.findChild(QtWidgets.QLineEdit, 'scatter_vmin')
        self.scatter_vmax = self.findChild(QtWidgets.QLineEdit, 'scatter_vmax')
        self.scatterplot_btn = self.findChild(QtWidgets.QPushButton, 'scatterplot_btn')


        self.column_list.clicked.connect(self.target)
        self.openPushButton.clicked.connect(self.openFile)
        self.submitButton.clicked.connect(self.set_target)
        self.scale_botton.clicked.connect(self.scale_value)
        self.convert_btn.clicked.connect(self.con_cat)
        self.drop_btn.clicked.connect(self.dropc)

        self.fill_na.clicked.connect(self.fill_na_value)
        self.fill_mean.clicked.connect(self.fill_mean_value)

        self.scatterplot_btn.clicked.connect(self.scatter_plot)

        self.show()


    def scatter_plot(self):
        x = self.scatter_x.currentText()
        y = self.scatter_y.currentText()
        c = self.scatter_c.currentText()
        mark = self.scatter_mark.currentText()

        # if self.scatter_vmin.text() == "":
        #     vmin = None
        # else:
        #     vmin = float(self.scatter_vmin.text())
        plt.figure()
        plt.scatter(self.df[x], self.df[y], c=c, marker=mark)
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(f'{x} vs {y}')
        plt.show()


    def fill_na_value(self):
        x = self.empty_column.currentText()
        self.df[x] = self.df[x].fillna('Unknown')
        self.fillDetails()


    def fill_mean_value(self):
        x = self.empty_column.currentText()
        self.df[x] = self.df[x].fillna(self.df[x].mean(), inplace=True)
        self.fillDetails()


    def dropc(self):
        x = self.drop_column.currentText()
        print(x)
        if (x == self.target_value):
            self.target_value = ""
            self.target_col.setText("")
        self.df = self.df.drop(x, axis=1)
        
        self.fillDetails()


    def con_cat(self):
        x = self.cat_column.currentText()
        le = LabelEncoder()
        self.df[x] = le.fit_transform(self.df[x]) # 해당 컬럼값이 숫자로 바뀌게 됨

        self.fillDetails()
        

    def scale_value(self):
        print(self.target_value)
        if self.target_value == None:
            print("set Target")
            if self.scaler.currentText() == "StandardScale":
                sc = StandardScaler()
                scaled_features = sc.fit_transform(self.df)
                # return scaled_features

            elif self.scaler.currentText() == "MinMaxScale":
                sc = MinMaxScaler()
                scaled_features = sc.fit_transform(self.df)
                # return scaled_features

            else:
                sc = PowerTransformer()
                scaled_features = sc.fit_transform(self.df)
                # return scaled_features

        else:
            x = self.df.drop(self.target_value, axis=1)
            if self.scaler.currentText() == "StandardScale":
                sc = StandardScaler()
                scaled_features = sc.fit_transform(x)
                scaled_df = pd.DataFrame(scaled_features, index = x.index, columns=x.columns)
                scaled_df[self.target_value] = self.df[self.target_value]
                print(scaled_df)
                self.df = scaled_df
                print(scaled_features)
                # return scaled_features

            elif self.scaler.currentText() == "MinMaxScale":
                sc = MinMaxScaler()
                scaled_features = sc.fit_transform(x)
                scaled_df = pd.DataFrame(scaled_features, index = x.index, columns=x.columns)
                scaled_df[self.target_value] = self.df[self.target_value]
                print(scaled_df)
                self.df = scaled_df
                print(scaled_features)
                # return scaled_features
            else:
                sc = PowerTransformer()
                scaled_features = sc.fit_transform(x)
                scaled_df = pd.DataFrame(scaled_features, index = x.index, columns=x.columns)
                scaled_df[self.target_value] = self.df[self.target_value]
                print(scaled_df)
                self.df = scaled_df
                print(scaled_features)
                # return scaled_features
            # print(x)
            # print(self.scaler.currentText())
        
        self.fillDetails()


    def set_target(self):
        if self.item == None:
            self.target_col.setText("Not Selected")
        else:
            self.target_value = self.item.text().split(" ")[0]
            self.target_col.setText(self.target_value)


    def target(self):
            self.item = self.column_list.currentItem()
            print(self.item.text())


    def fillDetails(self, flag = 1):
        if flag == 0:
            self.df = pd.read_csv(self.filePath)
            print(self.df.columns)

        for i, j in enumerate(self.df.columns):
            # enumerate() 쓰면 i에 인덱스, j에 해당 값이 오게 됨
            str = f"{j} -------  {self.df[j].dtype}"
            self.column_list.insertItem(i, str)
        # print(self.filePath)
        cat_col = []
        for i in self.df.columns:
            if (self.df[i].dtype == 'object'):
                cat_col.append(i)
        self.cat_col_list = cat_col
        print(self.cat_col_list)
        
        empty_col = []
        for i in self.df.columns:
            if (self.df[i].isna().values.any()==True):
                empty_col.append(i)
        self.empty_col_list = empty_col
        print(empty_col)
        self.fill_combo_box()


    def fill_combo_box(self):
        self.cat_column.clear()
        self.cat_column.addItems(self.cat_col_list)

        self.drop_column.clear()
        self.drop_column.addItems(self.df.columns)

        self.empty_column.clear()
        self.empty_column.addItems(self.empty_col_list)

        self.scatter_x.clear()
        self.scatter_x.addItems(self.df.columns)

        self.scatter_y.clear()
        self.scatter_y.addItems(self.df.columns)


        x = table_display.DataFrameModel(self.df)
        print(self.df.shape)
        self.shape.setText(f'Rows : {self.df.shape[0]}, Column : {self.df.shape[1]}')
        self.tableView.setModel(x)
    

    def openFile(self):
        self.filePath, _ =  QtWidgets.QFileDialog.getOpenFileName(self ,"Open File", "", "csv(*.csv)")
    #   print(self.filePath)
        self.column_list.clear()
        self.fillDetails(0)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = UI()
    sys.exit(app.exec_())  