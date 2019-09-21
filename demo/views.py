from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets

from demo.models import Book
from demo.serializers import BookSerializer

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
    serializer_class = BookSerializer
    queryset = Book.objects.all()