import pytube
import os
import shutil
from os import path
import random
from string import ascii_letters,punctuation
from django.conf import settings

from .models import FileSystem


def file_zipper(playlist_id):
    if path.exists(f'media/{playlist_id}'):
        src= path.realpath(f'media/{playlist_id}')

        shutil.make_archive(f'media/{playlist_id}_zip','zip',src)

        return f'media/{playlist_id}_zip'


def playlist_id_maker(playlist):
    
    playlist_title=(playlist.title).translate({ord(x): '' for x in punctuation}).replace(' ','_')
    return f'{playlist_title}_{"".join(random.choices(ascii_letters,k=7))}'

def deleteFolder(name):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    shutil.rmtree(os.path.join(BASE_DIR,'media',name),True)

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


def constructMediaLink(zipfile_name):
    media_link=f'http://localhost:8000/{zipfile_name}.zip'
    return media_link

def playlist_downloader(body):

    playlist=pytube.Playlist(body['url'])
    folder_name = playlist_id_maker(playlist)
    upper_limit=int(body['ul'])
    lower_limit=int(body['ll'])
    resolution=body['resolution']

    for url in playlist.video_urls[lower_limit:upper_limit]:
        youtube = pytube.YouTube(url)
        failSafeDownload(youtube,resolution,folder_name)

    zipfile_name = file_zipper(folder_name)
    
    deleteFolder(folder_name)
   
    
    return constructMediaLink(zipfile_name)



def single_download(body):
    youtube = pytube.YouTube(body['url'])
    folder_name =  playlist_id_maker(youtube)
    resolution = body['resolution']

    failSafeDownload(youtube,resolution,folder_name)

    zipfile_name = file_zipper(folder_name)
    deleteFolder(folder_name)

    return constructMediaLink(zipfile_name)
