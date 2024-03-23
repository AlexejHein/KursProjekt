from django.urls import path
from .views import index, PollDeteilView, ResultsDeteilView, vote

urlpatterns = [
    path('', index, name='index'),
    path('abstimmung/<str:slug>/', PollDeteilView.as_view(), name='umfrage_deteil'),
    path('abstimmung/<str:slug>/abstimmen/', vote, name='vote'),
    path('abstimmung/<str:slug>/results/', ResultsDeteilView.as_view(), name='results'),
]