from django.contrib import admin
from django.urls import path

from demo.views import first

urlpatterns = [
    path('firstfunction', first),
]
