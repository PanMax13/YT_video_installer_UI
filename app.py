# TODO:
#  1. do a app window
#  2. do a input field for yt-video link
#  3. connect with backend
import asyncio
from installer import install_data

from PyQt6.QtWidgets import QWidget, QApplication, QFormLayout, \
    QLabel, QLineEdit, QPushButton


class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("YouTube installer")
        self.resize(400, 200)

        self.inputLinkLine = QLineEdit()
        self.inputLinkLine.setText("Input the link")

        self.fileName = QLineEdit()
        self.fileName.setText("Enter your file name")

        doneButton = QPushButton(text="Done!")

        self.message = QLabel("")

        doneButton.clicked.connect(self.button_clicked)



        layout = QFormLayout()
        layout.addRow(self.inputLinkLine)
        layout.addRow(self.fileName)
        layout.addRow(doneButton)
        layout.addRow(self.message)

        self.setLayout(layout)

    def button_clicked(self):
        link = self.inputLinkLine.text()
        name = self.fileName.text()

        self.message.setText(asyncio.run(install_data(link, name)))



app = QApplication([])
window = Window()
window.show()
app.exec()