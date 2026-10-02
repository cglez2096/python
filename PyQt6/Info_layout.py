from PyQt6.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QLineEdit,QCheckBox,QMainWindow,QMessageBox,QHBoxLayout,QVBoxLayout,QGridLayout,QFormLayout,QComboBox,QTextEdit
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

        form_layout = QFormLayout()
        self.setLayout(form_layout)

        self.name_edit = QLineEdit()
        self.email_edit = QLineEdit()
        self.phone_edit = QLineEdit()

        self.subject_combo = QComboBox()
        self.subject_combo.addItems(["Select Subject: ", "Personal","Business"])

        self.message_edit = QTextEdit()

        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submit_clicked)

        form_layout.addRow(QLabel("Name: "), self.name_edit)
        form_layout.addRow(QLabel("Email: "), self.email_edit)
        form_layout.addRow(QLabel("Phone: "), self.phone_edit)

        form_layout.addRow(QLabel("Subject: "), self.subject_combo)
        form_layout.addRow(QLabel("Message: "), self.message_edit)
        form_layout.addRow(submit_button)

    def submit_clicked(self):
        name = self.name_edit.text()
        email = self.email_edit.text()
        phone = self.phone_edit.text()

        subject = self.subject_combo.currentText()
        message = self.message_edit.toPlainText()

        print(f" Name: {name} \n Email: {email} \n Phone: {phone} \n Subject: {subject} \n Message: {message}")







app = QApplication(sys.argv)
window = Window()

window.show()

sys.exit(app.exec())
