import asyncio
from installer import install_data, download_playlist

from PyQt6.QtWidgets import QWidget, QApplication, QFormLayout, \
    QLabel, QLineEdit, QPushButton, QFileDialog, QComboBox

from languages import lang

class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)


        self.combobox = QComboBox(self)

        for key in lang:
            self.combobox.addItem(key)

        self.language = lang[self.combobox.currentText()]
        print(self.language)
        self.setWindowTitle("YouTube installer")
        self.resize(400, 200)

        self.inputLinkLine = QLineEdit()

        self.fileName = QLineEdit()

        self.download_video_button = QPushButton(text=self.language['downloadVideo'])
        self.download_audio_button = QPushButton(text=self.language['downloadAudio'])
        self.download_playlist_vidios = QPushButton(text=self.language['downloadPlaylistVideo'])
        self.download_playlist_audios = QPushButton(text=self.language['downloadPlaylistAudio'])

        self.message = QLabel("")


        self.path = QFileDialog.getExistingDirectory(
            caption='Select a path to install',
            directory='./'
        )

        print(self.path)

        # making layout
        layout = QFormLayout()
        layout.addRow(self.inputLinkLine)
        layout.addRow(self.fileName)
        layout.addRow(self.download_audio_button, self.download_video_button)
        layout.addRow(self.download_playlist_audios, self.download_playlist_vidios)
        layout.addRow(self.message)
        layout.addRow(self.combobox)

        self.setLayout(layout)

        # call the functions
        self.combobox.currentIndexChanged.connect(self.changeLanguage)
        self.download_audio_button.clicked.connect(self.audio_button_clicked)
        self.download_video_button.clicked.connect(self.video_button_clicked)
        self.download_playlist_vidios.clicked.connect(self.playlist_video_button_clicked)
        self.download_playlist_audios.clicked.connect(self.playlist_audio_button_clicked)


        self.update_lang()



    def playlist_video_button_clicked(self):
        link = self.inputLinkLine.text()
        name = self.fileName.text()

        self.message.setText(asyncio.run(download_playlist(link, 'Carrousel', _type='video', path=self.path, _lang=self.combobox.currentText())))


    def playlist_audio_button_clicked(self):
        link = self.inputLinkLine.text()
        name = self.fileName.text()

        self.message.setText(asyncio.run(download_playlist(link, 'Carrousel', _type='audio', path=self.path, _lang=self.combobox.currentText())))


    def video_button_clicked(self):
        link = self.inputLinkLine.text()
        name = self.fileName.text()

        self.message.setText(asyncio.run(install_data(link, name, 'video', path=self.path, _lang=self.combobox.currentText())))

    def audio_button_clicked(self):
        link = self.inputLinkLine.text()
        name = self.fileName.text()

        self.message.setText(asyncio.run(install_data(link, name, 'audio', path=self.path, _lang=self.combobox.currentText())))

    def update_lang(self):
        self.language = lang[self.combobox.currentText()]
        self.inputLinkLine.setPlaceholderText(self.language["inputLinkButton"])
        self.fileName.setPlaceholderText(self.language["inputNameVideo"])
        self.download_video_button.setText(self.language["downloadVideo"])
        self.download_audio_button.setText(self.language["downloadAudio"])
        self.download_playlist_audios.setText(self.language['downloadPlaylistAudio'])
        self.download_playlist_vidios.setText(self.language['downloadPlaylistVideo'])

    def changeLanguage(self):
        self.update_lang()
        print('lang changed')


app = QApplication([])
window = Window()
window.show()
app.exec()