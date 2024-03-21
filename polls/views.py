from django.shortcuts import render

from .models import Poll, Choice


def index(request):
    context = {
        'umfragen': Poll.objects.all(),
        'title': "Umfragen",
    }
    return render(request, 'polls/index.html', context)
