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

def deleteFolder(name):
    return shutil.rmtree(name,True)

def failSafeDownload(youtube,resolution,folder_name):

    if resolution != 'audio':
        video=youtube.streams.get_by_resolution(resolution)
    else:
        video=youtube.streams.get_audio_only()

    if video:
        video.download(f'media/{folder_name}')
    else:
        if resolution=='360p' or resolution=='480':
            video=youtube.streams.get_lowest_resolution()
            video.download(f'media/{folder_name}')
        elif resolution == 'audio':
            video=youtube.streams.get_audio_only()
            video.download(f'media/{folder_name}')
        else:
            video=youtube.streams.get_highest_resolution()
            video.download(f'media/{folder_name}')

def playlist_downloader(body):

    playlist=pytube.Playlist(body['url'])
    folder_name = playlist_id_maker(playlist)
    upper_limit=body['ul']
    lower_limit=body['ll']
    resolution=body['resolution']

    for url in playlist.video_urls[lower_limit:upper_limit]:
        youtube = pytube.YouTube(url)
        failSafeDownload(youtube,resolution,folder_name)

    file_zipper(folder_name)
    deleteFolder(folder_name)


def single_download(body):
    youtube = pytube.YouTube(body['url'])
    folder_name =  youtube.title
    resolution = body['resolution']

    video=youtube.streams.get_by_resolution(resolution)
    video.download(f'media/{folder_name}')

    file_zipper(folder_name)
    deleteFolder(folder_name)