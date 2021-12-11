from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('library/', views.BooksLibrary, name='books_library'),
]