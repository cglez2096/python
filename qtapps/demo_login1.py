from PyQt6.QtWidgets import QRadioButton,QApplication,QMainWindow,QStyleFactory,QLabel, QVBoxLayout, QWidget,QPushButton,QGroupBox, QHBoxLayout,QTableWidget,QTabWidget,QCheckBox
import sys
from PyQt6.QtGui import QPixmap,QFont,QAction,QIcon,QTextCursor,QColor
import math
from PyQt6.QtCore import Qt
from demo_login_code import Ui_Form


class Window(QMainWindow):

    def __init__(self):
        
        super().__init__()
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(0,0,700,500)
        self.ui.lineEdit.setMaxLength(8)
        self.ui.lineEdit_2.setMaxLength(8)

        self.ui.pushButton.clicked.connect(self.check)

    def check(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if username == "admin" and password =="admin123":
            print("Valid username and password")
        else: 
            print("Invalid username and password")



        
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())