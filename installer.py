from pytubefix import YouTube
import os

async def install_data(link: str, file_name: str, _type: str, path: str): # get link of YT-video
    try:
        video = YouTube(link) # get video object

        if _type == 'audio':
            video = video.streams.get_audio_only() # get audio
        if _type == 'video':
            video = video.streams.get_highest_resolution()
            print(video)

        print(path)
        print(video)
        file = video.download(f'{path}') # install to dir
        print(file)
        os.rename(file, f"{path}/{file_name}.mp3") if _type == 'audio' else os.rename(file, f"{path}/{file_name}.mp4") # rename file

        return "Success"

    except Exception as e:
        print(e)
        return f"If you try caused error, check for link is valid or try to turn on VPN + \n {e}"

