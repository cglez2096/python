from PyQt6.QtWidgets import QRadioButton,QApplication,QMainWindow,QStyleFactory,QLabel, QVBoxLayout, QWidget,QPushButton,QGroupBox, QHBoxLayout,QTableWidget,QTabWidget,QCheckBox
import sys
from PyQt6.QtGui import QPixmap,QFont,QAction,QIcon,QTextCursor,QColor
import math
from PyQt6.QtCore import Qt


class Window(QWidget):

    def __init__(self):
        
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle("   D E S I G N E R     ")
        self.setGeometry(0,0,700,500)

        tab = QTabWidget()

        tea_tab = QWidget()
        coffe_tab = QWidget()

        tab.addTab(tea_tab,"Tea")
        tab.addTab(coffe_tab,"Coffe")

    #Tea layout
        tea_layout = QVBoxLayout()

        label = QLabel("Select Milk /  Water")
        milk_button = QRadioButton("Milk")
        water_button = QRadioButton("Water")

    #Container milk/water Group
        liquid_group = QGroupBox()

        liquid_layout = QVBoxLayout()

        liquid_layout.addWidget(milk_button)
        liquid_layout.addWidget(water_button)

        liquid_group.setLayout(liquid_layout)

        tea_layout.addWidget(label)
        tea_layout.addWidget(liquid_group)
        tea_tab.setLayout(tea_layout)

        #############################  S P I C E S #############

        label_spices = QLabel("Select Spices to add: ")
        tea_layout.addWidget(label_spices)

        spice_box = QGroupBox()

        spice_layout = QVBoxLayout()

        spice_box.setLayout(spice_layout)

        spices = ['Sugar','Clove','Black Pepper','Cinamon','Turmuric']
        for spice in spices:
            spice_check = QCheckBox(spice)
            spice_layout.addWidget(spice_check)


        
        tea_layout.addWidget(spice_box)
        #tea_tab.setLayout(spice_layout)


        main_layout = QVBoxLayout(self)
        main_layout.addWidget(tab)






        
app = QApplication(sys.argv)


window = Window()
print(QStyleFactory.keys())
print(app.style().name())
window.show()

sys.exit(app.exec())