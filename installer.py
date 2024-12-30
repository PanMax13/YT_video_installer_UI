from pytubefix import YouTube
import os
import asyncio

async def install_data(link: str, file_name: str): # get link of YT-video
    try:
        video = YouTube(link) # get video object
        video = video.streams.filter(only_audio=True) # get audio
        file = video[0].download('./') # install to dir

        os.rename(file, f"{file_name}.mp3") # rename file

        return "Success"

    except Exception as e:
        return "If you try caused error, check for link is valid or try to turn on VPN"

