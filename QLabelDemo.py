import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout


def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(320, 300) # Set window size
    # Center the window
    screen = app.primaryScreen().availableGeometry().center() # Get the centre point of the screen
    frame = window.frameGeometry() # Get the frame geometry of the window
    frame.moveCenter(screen)
    window.move(frame.topLeft()) # # Position window so its centre matches screen centre
    window.setWindowTitle("Demo App")
    main_layout = QVBoxLayout()
    # Row layout for label and input
    row = QHBoxLayout()
    text = QLabel("Enter your name: ")
    font = QFont()
    font.setPointSize(12)
    text.setFont(font)
    text.setAlignment(Qt.AlignLeft)
    name = QLineEdit()
    #name.setFixedWidth(350)
    name.setAlignment(Qt.AlignLeft)
    row.addWidget(text)
    row.addWidget(name)
    row.addStretch() # Extra space after input line
    main_layout.addLayout(row)
    window.setLayout(main_layout)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()