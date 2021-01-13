from django.shortcuts import render
import pytube
import os
import shutil
from os import path


# from pytube import YouTube

# playlist=pytube.Playlist('https://www.youtube.com/watch?v=sakQbeRjgwg&list=PL4cUxeGkcC9jdm7QX143aMLAqyM-jTZ2x&index=1')
# playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
# print(playlist)
# for url in playlist.video_urls:
#     youtube = pytube.YouTube(url)
#     print(youtube.streams.first())
    

# playlist=pytube.Playlist('https://www.youtube.com/playlist?list=PL4cUxeGkcC9hKBg2mU8Hat4-NedlubC3C')
# # playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
# for url in playlist.video_urls:
#     youtube = pytube.YouTube(url)
#     video = youtube.streams.first()
#     video.download('media/screen')
# python -m pip install git+https://github.com/nficano/pytube  correct pytube-plugin

def home(request):
    youtube = pytube.YouTube('https://www.youtube.com/watch?v=JLqsrofwPdI')
    video = youtube.streams.first()
    video.download('media')
    return render(request,'downloader/index.html')


def main():

    if path.exists('media/screen'):
        src= path.realpath('media/screen')
        print(src)

    root_dir,tail=path.split(src)
    shutil.make_archive('media/screen_zip','zip',src)

main()