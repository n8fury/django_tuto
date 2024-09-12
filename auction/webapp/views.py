from django.shortcuts import render


def hello(request, *args, **kwargs):
    return render(request, 'webapp/index.html', {})
# Create your views here.
