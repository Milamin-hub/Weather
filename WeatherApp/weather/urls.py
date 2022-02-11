from django.urls import path

from weather.views import *

urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name="about"),
    path('delete/<int:id>/', delete),
]