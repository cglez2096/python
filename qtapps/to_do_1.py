from PyQt6.QtWidgets import QRadioButton,QApplication,QMainWindow,QStyleFactory,QLabel, QVBoxLayout, QWidget,QPushButton,QGroupBox, QHBoxLayout,QTableWidget,QTabWidget,QCheckBox
import sys
from PyQt6.QtGui import QPixmap,QFont,QAction,QIcon,QTextCursor,QColor
import math
from PyQt6.QtCore import Qt
from to_do_list import Ui_Form

class Window(QMainWindow):

    def __init__(self):
        
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        
        self.initUI()

    def initUI(self):
        self.setGeometry(0,0,700,500)
        self.ui.add_button.clicked.connect(self.addtask)
        self.ui.delete_button.clicked.connect(self.deletetask)

    def addtask (self):
        task = self.ui.task_edit.text()

        if task:
            self.ui.list_widget.addItem(task)
            self.ui.task_edit.clear()

    def deletetask(self):
        selected_task = self.ui.list_widget.currentItem()
        if selected_task:
            self.ui.list_widget.takeItem(self.ui.list_widget.row(selected_task))



        
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())