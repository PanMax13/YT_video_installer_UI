from pytubefix import YouTube, Playlist
import os
from languages import lang

async def install_data(link: str, file_name: str, _type: str, path: str, _lang: str): # get link of YT-video

    language = lang[_lang]
    try:
        video = YouTube(link) # get video object

        if _type == 'audio':
            video = video.streams.get_audio_only() # get audio
        if _type == 'video':
            video = video.streams.get_highest_resolution()

        file = video.download(f'{path}') # install to dir
        os.rename(file, f"{path}/{file_name}.mp3") if _type == 'audio' else os.rename(file, f"{path}/{file_name}.mp4") # rename file

        return language['success']

    except Exception as e:
        print(e)
        return f"{language['err']} + \n {e}"



async def download_playlist(link: str, playlist_name: str, _type: str, path: str, _lang: str):
    language = lang[_lang]
    try:
        os.mkdir(path + f'/{playlist_name}')
        new_path = path + f'/{playlist_name}'
        playlist = Playlist(link)

        print(new_path)
        for video in playlist.videos:
            if _type == 'video':
                video = video.streams.get_highest_resolution()

                video.download(new_path)
            else:
                video = video.streams.get_audio_only()
                file = video.download(new_path)

                os.rename(file, f'{new_path}/{video.title}.mp3')


        return language['success']

    except Exception as e:
        return f"{language['err']} + \n {e}"
