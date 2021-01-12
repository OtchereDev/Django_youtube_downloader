from django.urls import path
from .views import home

app_name='ytb_downloader'

urlpatterns = [
    path('',home),
]
