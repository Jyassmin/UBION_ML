from PyQt5 import QtWidgets , uic , QtCore

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('uicodes/MLP.ui' , self)
        
        self.show()