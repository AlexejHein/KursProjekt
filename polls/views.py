from django.shortcuts import render
from django.http import HttpResponse

from .models import Poll, Choice


def index(request):
    antwort = ""
    for poll in Poll.objects.all():
        antwort += poll.name + "<br>"
        for choice in poll.choice_set.all():
            antwort += choice.name + "<br>"
    return HttpResponse(antwort)
