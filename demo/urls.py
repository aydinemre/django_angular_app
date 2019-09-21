from django.contrib import admin
from django.urls import path

from demo.views import first, Another

urlpatterns = [
    path('first', first),
    path('another', Another.as_view()),
]
