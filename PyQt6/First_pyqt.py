
from PyQt6.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QLineEdit,QCheckBox,QMainWindow,QMessageBox
import sys
from PyQt6.QtGui import QPixmap,QFont
import math

class Window(QMainWindow):

    def __init__(self):
        
        super().__init__()
        self.initUI()

    def initUI(self):
        self.count = 0

        self. setWindowTitle("M Y   F I R S T   P Y Q T    W I N D O W")
        self.setGeometry(0,0,400,400)

        number_label = QLabel("Enter number: ",self)
        number_label.move(20,20)

        self.number_input = QLineEdit(self)
        self.number_input.move(200,20)

        calculate_button = QPushButton("Find root ",self)
        calculate_button.move(200,60)

        self.result_label =QLabel("Result: ",self)
        self.result_label.resize(200,20)
        self.result_label.move(20,100)

        calculate_button.clicked.connect(self.operation)

    def operation(self):
        try:
            number = float(self.number_input.text())
            sqr_number = math.sqrt(number)

            if sqr_number.is_integer():
                self.result_label.setText(f"Sqr root = {sqr_number}")
            else:
                msg = QMessageBox.warning(self,"Not a perfect square", "The number is not a perfect square")
        except ValueError:
            QMessageBox.warning(self,"Invalid Input","Please enter a valid number")





app = QApplication(sys.argv)
window = Window()

window.show()

sys.exit(app.exec())


