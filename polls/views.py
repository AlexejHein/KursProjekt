from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Poll, Choice


def index(request):
    context = {
        'umfragen': Poll.objects.all(),
        'title': "Umfragen",
    }
    return render(request, 'polls/index.html', context)


def umfrage_deteil(request, slug):
    umfrage = get_object_or_404(Poll, slug=slug)
    context = {'umfrage': umfrage}
    return render(request, 'polls/umfrage.html', context)
