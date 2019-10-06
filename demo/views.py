from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from rest_framework.response import Response

from demo.models import Book
from demo.serializers import BookSerializer, BookMiniSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

"""
class Another(View):

    # books = Book.objects.all()
    # books = Book.objects.filter(is_published=True)
    book = Book.objects.get(id=1)

    #output = ''
    #for book in books:
    #    output += "We have {} book in DB".format(book.title)
    output = "We have {} book in DB".format(book.title)


    def get(self, request):
        print(self.output)
        return HttpResponse(self.output)


def first(request):
    books = Book.objects.all()
    # return HttpResponse("First message from views"
    return render(request, 'first_template.html', {"books": books})
"""


class BookViewSet(viewsets.ModelViewSet):
    # serializer_class = BookSerializer
    serializer_class = BookMiniSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)
