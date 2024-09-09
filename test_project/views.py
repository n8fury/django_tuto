from django.http import HttpResponse


def hello_world(request, *args, **kwargs):
    return HttpResponse('<h1>Hello, World!</h1>')
