from PyQt6.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QLineEdit,QCheckBox,QMainWindow,QMessageBox,QHBoxLayout,QVBoxLayout,QGridLayout,QFormLayout,QComboBox,QTextEdit,QStackedLayout
import sys
from PyQt6.QtGui import QPixmap,QFont,QAction,QIcon
import math
from PyQt6.QtCore import Qt

class Window(QMainWindow):

    def __init__(self):
        
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("      M  E  N  U     ")
        self.setGeometry(100,100,400,300)

        '''#Step 1 : Create menur Bar
        menubar = self.menuBar()

        #menu items
        file_menu = menubar.addMenu("File")

        #Creating action
        self.new_action = QAction("New")
        

        #Adding action to the menu
        file_menu.addAction(self.new_action)

        #Adding a separator
        file_menu.addSeparator()


        #Creating another Action
        self.exit_action = QAction("Exit")
        file_menu.addAction(self.exit_action)

        #Creating a new menu

        edit_menu = menubar.addMenu("Edit")

        self.copy_action = QAction("Copy")
        edit_menu.addAction(self.copy_action)
        edit_menu.addSeparator()

        self.cut_action = QAction("Cut")
        edit_menu.addAction(self.cut_action)
        edit_menu.addSeparator()

        self.paste_action = QAction("Paste")
        edit_menu.addAction(self.paste_action)
        edit_menu.addSeparator()'''

        # TOOLBAR MENU

        toolbar = self.addToolBar("Main Toolbar")

        self.new_action = QAction(QIcon("icons/add_icon.png"),"New")
        toolbar.addAction(self.new_action)

        self.open_action = QAction(QIcon("icons/copy.png"),"Open")
        toolbar.addAction(self.open_action)

        toolbar.addSeparator()

        self.save_action = QAction(QIcon("icons/save.png"),"Save")
        toolbar.addAction(self.save_action)

        




        
app = QApplication(sys.argv)
window = Window()

window.show()

sys.exit(app.exec())