from django.contrib import admin
from django.urls import path, include

# from demo.views import first
from rest_framework import routers

from demo.views import BookViewSet

router = routers.DefaultRouter()
router.register("books", BookViewSet)
urlpatterns = [
    path('', include(router.urls))
    # path('first', first),
    # path('another', Another.as_view()),
]
