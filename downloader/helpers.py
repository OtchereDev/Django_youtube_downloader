import pytube
import os
import shutil
from os import path
import random
from string import ascii_letters

def file_zipper(playlist_id):
    if path.exists(f'media/{playlist_id}'):
        src= path.realpath(f'media/{playlist_id}')

        shutil.make_archive(f'media/{playlist_id}_zip','zip',src)


def playlist_id_maker(playlist):
    return f'{playlist.title}_{"".join(random.choices(ascii_letters,k=7))}'


def playlist_downloader(body):

    playlist=pytube.Playlist(body['url'])
    folder_name = playlist_id_maker(playlist)

    for url in playlist.video_urls[:3]:
        youtube = pytube.YouTube(url)
        video=youtube.streams.get_by_resolution(body['resolution'])
        # print(youtube.streams)
        if video:
            video.download(f'media/{folder_name}')
        else:
            video=youtube.streams.get_highest_resolution()
            video.download(f'media/{folder_name}')

    file_zipper(folder_name)


def single_download(body):
    youtube = pytube.YouTube(body['url'])
    folder_name =  youtube.title
    video=youtube.streams.get_by_resolution(body['resolution'])
    video.download(f'media/{folder_name}')

    file_zipper(folder_name)