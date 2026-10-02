
from PyQt6.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QLineEdit,QCheckBox,QMainWindow,QMessageBox,QHBoxLayout,QVBoxLayout,QGridLayout
import sys
from PyQt6.QtGui import QPixmap,QFont
import math

class Window(QWidget):

    def __init__(self):
        
        super().__init__()
        self.initUI()

    def initUI(self):
        self.count = 0

        self. setWindowTitle("M Y   S E C O N D   P Y Q T    W I N D O W")
        self.setGeometry(0,0,400,400)

        label1 = QLabel("Label 1")
        label2 = QLabel("Label 2")
        label3 = QLabel("Label 3")

        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")

        layout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(label1,0,0)
        layout.addWidget(label2,0,1)
        layout.addWidget(label3,0,2)

        layout.addWidget(button1,1,0)
        layout.addWidget(button2,1,1)
        layout.addWidget(button3,1,2)


app = QApplication(sys.argv)
window = Window()

window.show()

sys.exit(app.exec())




