# TODO:
#  1. do a app window
#  2. do a input field for yt-video link
#  3. connect with backend
import asyncio
from installer import install_data

from PyQt6.QtWidgets import QWidget, QApplication, QFormLayout, \
    QLabel, QLineEdit, QPushButton, QFileDialog


class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("YouTube installer")
        self.resize(400, 200)

        self.inputLinkLine = QLineEdit()
        self.inputLinkLine.setText("Input the link")

        self.fileName = QLineEdit()
        self.fileName.setText("Enter your file name")

        download_video_button = QPushButton(text="Download video")
        download_audio_button = QPushButton(text="Download audio")

        self.message = QLabel("")

        download_audio_button.clicked.connect(self.audio_button_clicked)
        download_video_button.clicked.connect(self.video_button_clicked)

        self.path = QFileDialog.getExistingDirectory(
            caption='Select a path to install',
            directory='./'
        )

        layout = QFormLayout()
        layout.addRow(self.inputLinkLine)
        layout.addRow(self.fileName)
        layout.addRow(download_audio_button, download_video_button)
        layout.addRow(self.message)

        self.setLayout(layout)

    def video_button_clicked(self):
        link = self.inputLinkLine.text()
        name = self.fileName.text()

        self.message.setText(asyncio.run(install_data(link, name, 'video', path=self.path)))

    def audio_button_clicked(self):
        link = self.inputLinkLine.text()
        name = self.fileName.text()

        self.message.setText(asyncio.run(install_data(link, name, 'audio', path=self.path)))


app = QApplication([])
window = Window()
window.show()
app.exec()