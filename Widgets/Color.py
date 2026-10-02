from PyQt6.QtWidgets import QWidget,QApplication,QSlider,QLabel,QHBoxLayout,QVBoxLayout,QColorDialog
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
import sys


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def update_color(self):
        red = self.red_slider.value()
        green = self.green_slider.value()
        blue = self.blue_slider.value()

        self.color = QColor(red,green,blue)

        self.color_preview.setStyleSheet(f"background-color:{self.color.name()}")

        self.red_value_label.setText(str(red))
        self.green_value_label.setText(str(green))
        self.blue_value_label.setText(str(blue))

        self.final_label.setText(f"Final Color:{self.color.name()}")

    def show_color_dialog(self, event):
        
        if event.button() == Qt.MouseButton.LeftButton:
            color_dialog = QColorDialog(self.color,self)
            color_dialog.colorSelected.connect(self.set_color)
            color_dialog.exec()

    def set_color(self,color):
        self.color = color
        self.red_slider.setValue(color.red())
        self.green_slider.setValue(color.green())
        self.blue_slider.setValue(color.blue())

        self.update_color()


        


    def initUI (self):
        self.setGeometry(0,0,700,500)

        self.red_slider = QSlider(Qt.Orientation.Horizontal)
        self.green_slider = QSlider(Qt.Orientation.Horizontal)
        self.blue_slider = QSlider(Qt.Orientation.Horizontal)

        for slider in [self.red_slider,self.green_slider,self.blue_slider]:
            slider.setRange(0,255)
            slider.setValue(255)
            slider.setTickPosition(QSlider.TickPosition.TicksBelow)
            slider.setTickInterval(25)

        self.red_label = QLabel("RED: ")
        self.green_label = QLabel("GREEN: ")
        self.blue_label = QLabel("BLUE: ")

        self.red_value_label = QLabel("255")
        self.green_value_label = QLabel("255")
        self.blue_value_label = QLabel("255")

        #creating main windows layout
        layout = QVBoxLayout(self)

        sliders_layout = QVBoxLayout()

        for label,slider,value_label in zip([self.red_label,self.green_label,self.blue_label],
            [self.red_slider, self.green_slider, self.blue_slider],
            [self.red_value_label, self.green_value_label, self.blue_value_label]
            ):

            slider_layout = QHBoxLayout()
            slider_layout.addWidget(label)
            slider_layout.addWidget(slider)
            slider_layout.addWidget(value_label)

            sliders_layout.addLayout(slider_layout)

             
        layout.addLayout(sliders_layout)

        #Create a label for displayin of previewing of the color
        self.color_preview = QLabel()

        color_layout = QVBoxLayout()
        color_layout.addWidget(self.color_preview)
        color_layout.addStretch()
        layout.addLayout(color_layout)


        #Connecting sliders to method
        self.red_slider.valueChanged.connect(self.update_color)
        self.green_slider.valueChanged.connect(self.update_color)
        self.blue_slider.valueChanged.connect(self.update_color)


        #Setting the initial value of color
        self.color = "#ffffff"
        self.color_preview.setStyleSheet(f"background-color:{self.color}")
        self.color_preview.mousePressEvent = self.show_color_dialog

        self.final_label = QLabel("Final color = #ffffff")
        final_layout = QHBoxLayout()
        final_layout.addWidget(self.final_label)
        layout.addLayout(final_layout)







app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
