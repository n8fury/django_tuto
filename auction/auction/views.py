from django.http import HttpResponse
from django.shortcuts import render


def hello(request,*args,**kwargs):
    html_template = "hello.html"
    return render(request, html_template, {})