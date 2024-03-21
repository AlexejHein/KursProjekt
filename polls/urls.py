from django.urls import path
from .views import index, umfrage_deteil

urlpatterns = [
    path('', index, name='index'),
    path('abstimmung/<str:slug>/', umfrage_deteil, name='umfrage_deteil'),
]