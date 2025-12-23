# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
import sys


def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(300,250)
    window.setWindowTitle("Error!")
    window.show()
    label = QLabel("Your system will shut down immediately!")
    label.setStyleSheet("font-size: 20px, color: orange;")
    layout = QVBoxLayout()
    layout.addWidget(label)
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
