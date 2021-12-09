from django.shortcuts import render
from django.views import generic, View


def index(request):

    return render(request, 'index.html')


class BooksLibrary(View):

    def library(request):

      return render(request, 'library.html')
