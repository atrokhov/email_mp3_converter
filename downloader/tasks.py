# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import youtube_dl
import requests
import json
from django.conf import settings
from django.core.mail import send_mail
from celery import shared_task
from youtube_dl import YoutubeDL

@shared_task(name='download')
def download(url, email):
    ydl_opts = {
        'format': 'bestaudio/best',
        'audio-format': 'mp3',
        'outtmpl': 'media/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'quiet': True,
        'restrictfilenames': True
    }

    with YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(url)

    generated_mp3 = '{domain}{path}{filename}{format}'.format(
            domain='http://127.0.0.1:8000',
            path=settings.MEDIA_URL,
            filename=video_info['title'],
            format='.mp3'
        )

    title = "Скачайте MP3"

    message = '''
            Мы скачали MP3 из этого видео - %s
            Ссылка на скачивание MP3 - %s
        ''' % (url, generated_mp3)

    send_mail(title, message, settings.EMAIL_HOST_USER, [email], fail_silently=False,)