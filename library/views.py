from django.shortcuts import render
from django.views import generic, View


def library(request):

      return render(request, 'library.html')

