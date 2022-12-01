from PyQt5 import QtWidgets , uic , QtCore
import pandas as pd
import sys
import table_display
from sklearn.preprocessing import StandardScaler , MinMaxScaler , PowerTransformer , LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
import gui_linear_reg
import gui_logistic_reg
import gui_random_forest
import gui_knn
import gui_svm
import gui_Gau_NB
import gui_MLP



class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('uicodes/Mainwindow.ui' , self)
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

        self.empty_column = self.findChild(QtWidgets.QComboBox, 'empty_column')
        self.fill_mean = self.findChild(QtWidgets.QPushButton, 'fill_mean')
        self.fill_na = self.findChild(QtWidgets.QPushButton, 'fill_na')

        # scatter plot part 
        self.scatter_x = self.findChild(QtWidgets.QComboBox, 'scatter_x')
        self.scatter_y = self.findChild(QtWidgets.QComboBox, 'scatter_y')
        self.scatter_c = self.findChild(QtWidgets.QComboBox, 'scatter_c')
        self.scatter_mark = self.findChild(QtWidgets.QComboBox, 'scatter_mark')
        self.scatter_vmin = self.findChild(QtWidgets.QLineEdit, 'scatter_vmin')
        self.scatter_vmax = self.findChild(QtWidgets.QLineEdit, 'scatter_vmax')
        self.scatterplot_btn = self.findChild(QtWidgets.QPushButton, 'scatterplot')

        # line plot part 
        self.plot_x = self.findChild(QtWidgets.QComboBox, 'plot_x')
        self.plot_y = self.findChild(QtWidgets.QComboBox, 'plot_y')
        self.plot_c = self.findChild(QtWidgets.QComboBox, 'plot_c')
        self.plot_mark = self.findChild(QtWidgets.QComboBox, 'plot_marker')
        self.plot_vmin = self.findChild(QtWidgets.QLineEdit, 'plot_vmin')
        self.plot_vmax = self.findChild(QtWidgets.QLineEdit, 'plot_vmax')
        self.lineplot_btn = self.findChild(QtWidgets.QPushButton, 'lineplot')

        #histogram plot part
        self.hist_column = self.findChild(QtWidgets.QComboBox, 'hist_column')
        self.hist_column_add = self.findChild(QtWidgets.QComboBox, 'hist_column_add') 
        self.hist_add_btn = self.findChild(QtWidgets.QPushButton, 'hist_add_btn')
        self.hist_remove_btn = self.findChild(QtWidgets.QPushButton, 'hist_remove_btn')
        self.hist_bin = self.findChild(QtWidgets.QLineEdit, 'hist_bin')
        self.hist_x = self.findChild(QtWidgets.QLineEdit, 'hist_x')
        self.hist_y = self.findChild(QtWidgets.QLineEdit, 'hist_y')
        self.histogram_btn = self.findChild(QtWidgets.QPushButton, 'histogram')
        
        # histogram plot part
        self.heatmap = self.findChild(QtWidgets.QPushButton, 'heatmap')
        

        #QComboBox
        self.model_select = self.findChild(QtWidgets.QComboBox, "model_select")
        self.train_btn = self.findChild(QtWidgets.QPushButton, 'train')

        self.columnList.clicked.connect(self.target)
        self.openPushButton.clicked.connect(self.openFile)
        self.submitButton.clicked.connect(self.set_target)
        self.scale_btn.clicked.connect(self.scale_value)
        self.convert_btn.clicked.connect(self.con_cat)

        self.fill_na.clicked.connect(self.fill_na_value)
        self.fill_mean.clicked.connect(self.fill_mean_value)

        self.drop_btn.clicked.connect(self.dropc)


        self.scatterplot_btn.clicked.connect(self.scatter_plot)
        self.lineplot_btn.clicked.connect(self.line_plot)
        self.hist_add_btn.clicked.connect(self.hist_add_column)
        self.hist_remove_btn.clicked.connect(self.hist_remove_column)
        self.histogram_btn.clicked.connect(self.histogram_plot)
        self.heatmap.clicked.connect(self.heatmap_plot)
        self.train_btn.clicked.connect(self.train_model)
        self.show()


    def train_model(self):
        model = self.model_select.currentText()
        if model == 'Linear Regression':
            if self.target_value == 'None':
                dig = QtWidgets.QDialog(self)
                dig.setWindowTitle('Not set label')
                dig.resize(300, 200)
                dig.exec_()
            else:
                self.second = gui_linear_reg.UI(self.df, self.target_value, self.columnList)

        elif model == 'Logistic Regression':
            if self.target_value == 'None':
                dig = QtWidgets.QDialog(self)
                dig.setWindowTitle('Not set label')
                dig.resize(300, 200)
                dig.exec_()
            else:
                self.second = gui_logistic_reg.UI()

        elif model == 'Random Forest':
            if self.target_value == 'None':
                dig = QtWidgets.QDialog(self)
                dig.setWindowTitle('Not set label')
                dig.resize(300, 200)
                dig.exec_()
            else:
                self.second = gui_random_forest.UI()

        elif model == 'K-Nearest Neighbor':
            if self.target_value == 'None':
                dig = QtWidgets.QDialog(self)
                dig.setWindowTitle('Not set label')
                dig.resize(300, 200)
                dig.exec_()
            else:
                self.second = gui_knn.UI()

        elif model == 'SVM':
            if self.target_value == 'None':
                dig = QtWidgets.QDialog(self)
                dig.setWindowTitle('Not set label')
                dig.resize(300, 200)
                dig.exec()
            else:
                self.second = gui_svm.UI()

        elif model == 'Gaussian NB':
            if self.target_value == 'None':
                dig = QtWidgets.QDialog(self)
                dig.setWindowTitle('Not set label')
                dig.resize(300, 200)
                dig.exec_()
            else:
                self.second = gui_Gau_NB.UI()

        elif model == 'Multi Layer Perceptron':
            if self.target_value == 'None':
                dig = QtWidgets.QDialog(self)
                dig.setWindowTitle('Not set label')
                dig.resize(300, 200)
                dig.exec_()
            else:
                self.second = gui_MLP.UI()

        else:
            self.show_dialog('please select a model')


    def heatmap_plot(self):
        plt.figure(figsize=(10,10))
        x = self.df.corr()
        sns.heatmap(x , annot=True)
        plt.show()


    def hist_add_column(self):
        self.hist_column_add.addItem(self.hist_column.currentText())
        self.hist_column.removeItem(self.hist_column.findText(self.hist_column.currentText()))

    def hist_remove_column(self):
        self.hist_column.addItem(self.hist_column_add.currentText())
        self.hist_column_add.removeItem(self.hist_column_add.findText(self.hist_column_add.currentText()))

    def histogram_plot(self):
        AllItems = [self.hist_column_add.itemText(i) for i in range(self.hist_column_add.count())]
        for i in AllItems:
            self.df.hist(i)
            plt.show()

    def line_plot(self):
        x = self.plot_x.currentText()
        y = self.plot_y.currentText()
        c = self.plot_c.currentText()
        mark = self.plot_mark.currentText()

        # if self.plot_vmin.text() == "":
        #     vmin = None
        # else:
        #     vmin = float(self.plot_vmin.text())
        plt.figure()
        plt.plot(self.df[x] , self.df[y] , c = c, marker=mark)
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(f'{x} vs {y}')
        plt.show()

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
        plt.scatter(self.df[x] , self.df[y] , c = c, marker=mark)
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(f'{x} vs {y}')
        plt.show()
    def fill_na_value(self):
        x = self.empty_column.currentText()
        self.df[x] = self.df[x].fillna("Unknown")
        self.fillDetails()

    def fill_mean_value(self):
        x = self.empty_column.currentText()
        self.df[x].fillna(self.df[x].mean() , inplace=True)
        self.fillDetails()


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
        self.columnList.clear()
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

        empty_col = []
        for i in self.df.columns:
            if (self.df[i].isna().values.any()==True):
                empty_col.append(i)
        self.empty_col_list = empty_col
        print(self.empty_col_list)

        numeric_col = []
        for i in self.df.columns:
            if (self.df[i].dtype !='object'):
                numeric_col.append(i)

        self.numeric_col_list = numeric_col
        print(self.numeric_col_list)


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

        self.plot_x.clear() 
        self.plot_x.addItems(self.df.columns)

        self.plot_y.clear() 
        self.plot_y.addItems(self.df.columns)

        self.hist_column.clear() 
        self.hist_column.addItems(self.numeric_col_list)
        self.hist_column.addItem("All")

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