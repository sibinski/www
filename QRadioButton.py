from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QGridLayout
import sys

class RadioButton(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        radio = QRadioButton("Male")
        radio.setChecked(True)
        radio.gender = "Male"
        radio.toggled.connect(self.onClicked)
        layout.addWidget(radio, 0, 0)

        radio = QRadioButton("Female")
        radio.gender = "Female"
        radio.toggled.connect(self.onClicked)
        layout.addWidget(radio, 0, 1)

        radio = QRadioButton("Other")
        radio.gender = "Other"
        radio.toggled.connect(self.onClicked)
        layout.addWidget(radio, 0, 2)

    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            print(f"Gender is {radioButton.gender}")

app = QApplication(sys.argv)
window = RadioButton()
window.setWindowTitle("Radio Button Demo Application")
window.show()
sys.exit(app.exec_())

