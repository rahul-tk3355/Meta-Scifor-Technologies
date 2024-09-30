from django.shortcuts import render
import yt_dlp as youtube_dl
import os
from django.conf import settings

def youtube(request):
    if request.method == 'POST':
        link = request.POST['link']

        # Set the download path to a 'downloads' directory inside the project folder
        download_path = os.path.join(settings.BASE_DIR, 'downloads')
        os.makedirs(download_path, exist_ok=True)  # Create the directory if it doesn't exist

        ydl_opts = {
            'format': 'best[ext=mp4]', 
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),

        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        
        return render(request, 'youtube.html', {'message': 'Download complete'})

    return render(request, 'youtube.html')


