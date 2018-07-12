# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .forms import LinkForm
from .models import Link
from .tasks import download
from django.http import HttpResponsePermanentRedirect
from wsgiref.util import FileWrapper

import os


def index(request):
    latest_link_list = Link.objects.order_by('-pub_date')
    context = {'latest_link_list': latest_link_list}
    return render(request, 'downloader/index.html', context)

def download_song(request):
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            url = link.link_text
            email = link.user_email
            link.save()

            download.delay(url, email)
    else:
        form = LinkForm()
    return render(request, 'downloader/link_new.html', {'form': form})

def download_from_server(request, file_name):
    content_type = 'application/force-download'
    file_path = os.path.join(store_path, file_name)
    response = HttpResponse(FileWrapper(file(file_path)), content_type=content_type)
    response['Content-Disposition'] = 'attachment; filename=%s' % (
        file_name.encode('utf-8') if isinstance(filename, unicode) else file_name,
    )
    response['Content-Length'] = os.path.getsize(path)
    return response