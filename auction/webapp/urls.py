from django.urls import path
from . import views
urlpatterns = [
    path('', views.hello, name=''),
    path('register', views.register, name='register')
]
