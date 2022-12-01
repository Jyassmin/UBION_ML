from PyQt5 import QtWidgets , uic , QtCore

class UI(QtWidgets.QMainWindow):
    def __init__(self, df, target, columnList):
        super(UI, self).__init__()
        uic.loadUi('uicodes/RandomForest.ui' , self)
        self.X = df
        self.n_classes = self.X[str(target)].unique()
        self.target_value = str(target)
        self.X = self.X.drop(self.target_value, axis=1)
        self.columnList = columnList
        
        
        print(self.columnList)
        self.show()