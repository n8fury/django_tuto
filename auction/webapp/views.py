from django.shortcuts import render


def hello(request, *args, **kwargs):
    return render(request, 'webapp/home.html', {})
# Create your views here.
