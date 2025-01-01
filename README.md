# YT_video_installer_UI

# Языки/Languages:
### [Русский 🇷🇺](#Русский)
### [English 🇬🇧](#English)



# <a id="Русский">Русский🇷🇺</a>

Это приложение было создано для того, чтобы упростить жизнь пользователям, творческим людям и прочим. Оно позволяет скачать видео с ютюба или его звуковую дорожку. 
К сожалению, приложение пока поддерживает только русский и английский языки, но в дальнейшем будет добавлена поддержка других языков.

### Использование:
1. Клонируем репозиторий
```commandline
git clone https://github.com/PanMax13/YT_video_installer_UI.git 
```
2. Включаем среду разработки и скачиваем пакеты:
```
#  Для MacOs:
cd YT_video_installer_UI
source venv/bin/activate
pip3 install -r requirements.txt

# Для Windows: 
dir .\YT_video_installer_UI
virtualenv --python .\ venv
pip install -r requirements.txt
```

3. Активируем программу:

```commandline
# MacOS:
python3 app.py

# Windows: 
py app.py
```

4. Далее появяляется окно с выбором дирректории для скачивания файлов
5. Далее появляется окно приложения с двуми полями ввода: первое - ссылка на видео, второе - название для скачанного файла. Первые две кнопки по горизонтали: первая - качивает видео, вторая - скачивает аудиодорожку. Вторые две - отвечают за скачивание аудио и видел из плейлистов
6. Надписи, которые появляются внизу окна являются индикаторами ошибки и пишут результат выполнения программы

## Важно!!!!
#### В некоторых странах где YouTube заблокирован, приложение может работать некоректно.



# <a name="English">English🇬🇧</a>
This app was created for do life of users, createive people and other is easer. It be able to instal video from YouTube or audio from this video. Unfortunetaly, this app is support just Russian and English now, but in future support of other languages will be added

### Usage: 
1. Clone this repository: 
```commandline
git clone https://github.com/PanMax13/YT_video_installer_UI.git 
```
2. Turn on python venv:
```
#  fot MacOs:
cd YT_video_installer_UI
source venv/bin/activate
pip3 install -r requirements.txt

# for Windows: 
dir .\YT_video_installer_UI
virtualenv --python .\ venv
pip install requirements.txt
```

3. Activate the program:

```commandline
# MacOS:
python3 app.py

# Windows: 
py app.py
```

4. Then the window with choice of directory for install files will show
5. After window of app is open. It include 2 input field and 4 buttons. First input for link of YT-video, second - for title of installed file. Frist 2 buttons in horizontal for download audio or video from one YT-video, second 2 buttons in horizontal for download audios and vidios from palylists
6. Messages, which show in bottom of app's window - is messages about result of download


## Important!!!!
#### In some countries, when YT is blocked, app can work incorrect
