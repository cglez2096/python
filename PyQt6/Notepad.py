from PyQt6.QtWidgets import QInputDialog,QFileDialog,QMenu,QMenuBar,QWidget,QApplication,QLabel,QPushButton,QLineEdit,QCheckBox,QMainWindow,QMessageBox,QHBoxLayout,QVBoxLayout,QGridLayout,QFormLayout,QComboBox,QTextEdit,QStackedLayout
import sys
from PyQt6.QtGui import QPixmap,QFont,QAction,QIcon,QTextCursor,QColor
import math
from PyQt6.QtCore import Qt

class Window(QMainWindow):

    def __init__(self):
        
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("   N O T E P A D     ")
        self.setGeometry(100,100,400,300)

        self.current_file = None

        self.edit_field = QTextEdit(self)
        self.setCentralWidget(self.edit_field)

        #Create menu bar
        menu_bar = QMenuBar(self)
        menu_bar.setNativeMenuBar(False)
        self.setMenuBar(menu_bar)

        #Creating Menu
        file_menu = QMenu("File",self)
        menu_bar.addMenu(file_menu)



        #Create actions
        new_action = QAction("New",self)
        file_menu.addAction(new_action)
        new_action.triggered.connect(self.new_file)

        open_action = QAction("Open",self)
        file_menu.addAction(open_action)
        open_action.triggered.connect(self.open_file)

        save_action = QAction("Save",self)
        file_menu.addAction(save_action)
        save_action.triggered.connect(self.save_file)

        save_as_action = QAction("Save As..",self)
        file_menu.addAction(save_as_action)
        save_as_action.triggered.connect(self.save_as_file)

        #Creating the EDIT Menu

        edit_menu = QMenu("Edit",self)
        menu_bar.addMenu(edit_menu)

        #ACTIONS FOR EDIT  MENU
        undo_action = QAction("Undo",self)
        edit_menu.addAction(undo_action)
        undo_action.triggered.connect(self.edit_field.undo)

        redo_action = QAction("Redo",self)
        edit_menu.addAction(redo_action)
        redo_action.triggered.connect(self.edit_field.redo)

        copy_action = QAction("Copy",self)
        edit_menu.addAction(copy_action)
        copy_action.triggered.connect(self.edit_field.copy)

        cut_action = QAction("Cut",self)
        edit_menu.addAction(cut_action)
        cut_action.triggered.connect(self.edit_field.cut)

        paste_action = QAction("Paste",self)
        edit_menu.addAction(paste_action)
        paste_action.triggered.connect(self.edit_field.paste)

        find_action =QAction("Find",self)
        edit_menu.addAction(find_action)
        find_action.triggered.connect(self.find_text)




    def new_file(self):
        print("CREATING NEW FILE")

        self.edit_field.clear()
        self.current_file = None




    def open_file(self):
        print("OPENING A FILE ")
        file_path,_= QFileDialog.getOpenFileName(self, "Open file","","All Files (*);; Python Files(*.py)")
        with open(file_path, "r") as file:
            text = file.read()
            self.edit_field.setText(text)



    def save_as_file(self):

        print("SAVING FILE")
        file_path,_ = QFileDialog.getSaveFileName(self, "Save File", "", "All files(*);; Python File(*.py)")
        print(file_path)
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.edit_field.toPlainText())
            self.current_file = file_path
            



    def save_file(self):
        if self.current_file:
            with open (self.current_file,"w") as file:
                file.write(self.edit_field.toPlainText())
        else:
            self.save_as_file()

        print("SAVE FILE")

    def find_text(self):
        print("Finding Text")

        search, ok = QInputDialog.getText(self,"Find Text", "Search for")
        if ok:
            all_words=[]
            self.edit_field.moveCursor(QTextCursor.MoveOperation.Start)
            highlight_color = QColor(Qt.GlobalColor.yellow)

            while(self.edit_field.find(search)):
                selection = QTextEdit.ExtraSelection()
                selection.format.setBackground(highlight_color)

                selection.cursor = self.edit_field.textCursor()
                all_words.append(selection)
            self.edit_field.setExtraSelections(all_words)

        

        
app = QApplication(sys.argv)
window = Window()

window.show()

sys.exit(app.exec())