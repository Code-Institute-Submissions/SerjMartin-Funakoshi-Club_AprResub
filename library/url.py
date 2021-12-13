from django.urls import path
from . import views

urlpatterns = [
    path('', views.library, name='books_library'),
]
