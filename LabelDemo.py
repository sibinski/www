import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDesktopWidget, QVBoxLayout


def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(320, 300) # Set window size
    qr = window.frameGeometry() # Get the frame geometry of the window
    cp = QDesktopWidget().availableGeometry().center() # Get the centre point of the screen
    qr.moveCenter(cp)
    window.move(qr.topLeft()) # # Position window so its centre matches screen centre
    window.setWindowTitle("Label Demo App")
    text = QLabel(window)
    font = QFont()
    font.setPointSize(14)
    text.setFont(font)
    text.setText("PyQt Application Test.")
    text.setAlignment(Qt.AlignCenter)
    layout = QVBoxLayout()
    layout.addWidget(text)
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()