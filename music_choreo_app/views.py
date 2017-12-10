# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from models import *

def index(request):
    return render(request, 'music_choreo_app/index.html', {'programs': Program.objects.all()})

def release(request, program_token, release_number):
	return render(request, 'music_choreo_app/release.html', {'release': get_object_or_404(Release, program__name = program_token, number = release_number)})


