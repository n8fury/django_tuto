import pathlib
from django.http import HttpResponse
from django.shortcuts import render
this_dir = pathlib.Path(__file__).resolve().parent

def home(request, *args, **kwargs):
    html_template = "home.html"
    return render (request, html_template)

def old_home(request, *args, **kwargs):
    html_file = this_dir/"home.html"
    html_ = html_file.read_text()
    return HttpResponse(html_)

def hello_world(request, *args, **kwargs):
    return HttpResponse('<h1>Hello, World!</h1>')