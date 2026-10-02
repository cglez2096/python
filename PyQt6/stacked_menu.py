from PyQt6.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QLineEdit,QCheckBox,QMainWindow,QMessageBox,QHBoxLayout,QVBoxLayout,QGridLayout,QFormLayout,QComboBox,QTextEdit,QStackedLayout
import sys
from PyQt6.QtGui import QPixmap,QFont
import math
from PyQt6.QtCore import Qt

class Window(QWidget):

    def __init__(self):
        
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(" F O R M   L A Y O U T ")
        self.setGeometry(100,100,400,300)

        combo_box = QComboBox()
        combo_box.addItems(["Label","Form"])
        combo_box.activated.connect(self.change_page)

        #Creating page 1
        label =QLabel("This is the label page")

        #Creating page 2
        form = QFormLayout()
        form.addRow("", QLabel("This is a form page"))
        page2_container = QWidget()
        page2_container.setLayout(form)


        #creating a stacked layout
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(label)
        self.stacked_layout.addWidget(page2_container)

        main_layout = QVBoxLayout()
        main_layout.addWidget(combo_box)
        main_layout.addLayout(self.stacked_layout)

        self.setLayout(main_layout)

    def change_page(self,index):
        self.stacked_layout.setCurrentIndex(index)




        
app = QApplication(sys.argv)
window = Window()

window.show()

sys.exit(app.exec())