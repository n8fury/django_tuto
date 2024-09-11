from django.shortcuts import render


def hello(request, *args, **kwargs):
    return render(request, 'home.html', {})
# Create your views here.
