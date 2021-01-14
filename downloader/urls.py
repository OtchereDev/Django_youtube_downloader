from django.urls import path
from .views import home,downloader

app_name='ytb_downloader'

urlpatterns = [
    path('',home),
    path('video-download',downloader),
]
