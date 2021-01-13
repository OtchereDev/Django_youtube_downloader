import pytube
import os
import shutil
from os import path
import random
from string import ascii_letters

def file_zipper(playlist_id):
    if path.exists(f'media/{playlist_id}'):
        src= path.realpath(f'media/{playlist_id}')

        shutil.make_archive('media/screen_zip','zip',src)


def playlist_id_maker(playlist):
    return f'{playlist.title}_{random.choices(ascii_letters,7)}'


def playlist_downloader(body):

    playlist=pytube.Playlist(body.url)
    folder_name = playlist_id_maker(playlist)

    for url in playlist.video_urls:
        youtube = pytube.YouTube(url)
        video=youtube.streams.get_by_resolution(body.resolution)
        video.download(f'media/{folder_name}')

    file_zipper(folder_name)


def single_download(body):
    youtube = pytube.YouTube(body.url)
    folder_name =  youtube.title
    video=youtube.streams.get_by_resolution(body.resolution)
    video.download(f'media/{folder_name}')

    file_zipper(folder_name)