from django.urls import path
from .views import index, umfrage_deteil, vote, results

urlpatterns = [
    path('', index, name='index'),
    path('abstimmung/<str:slug>/', umfrage_deteil, name='umfrage_deteil'),
    path('abstimmung/<str:slug>/abstimmen/', vote, name='vote'),
    path('abstimmung/<str:slug>/results/', results, name='results'),
]