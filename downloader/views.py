from django.shortcuts import render
from django.http import JsonResponse
from .helpers import (file_zipper,playlist_id_maker,
                    playlist_downloader,single_download)
from django.views.decorators.csrf import csrf_exempt

from pytube import YouTube
import json

def home(request):

    return render(request,'downloader/index.html')

@csrf_exempt
def downloader(request):
    

    if request.method=='POST':
        body=json.loads(request.body)
        
        if body['playlist']:           
            media_link = playlist_downloader(body)

        else:
            media_link = single_download(body)

        return JsonResponse({'message':'it worked','media':media_link})   



# main()