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


def vote(request, slug):
    umfrage = get_object_or_404(Poll, slug=slug)
    try:
        ausgewahlte_antwort = umfrage.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return HttpResponse("Fehler: Keine Antwort ausgewählt.")
    else:
        ausgewahlte_antwort.votes += 1
        ausgewahlte_antwort.save()
        return HttpResponse("Danke fürs Abstimmen!")


def results(request, slug):
    umfrage = get_object_or_404(Poll, slug=slug)
    context = {'umfrage': umfrage}
    return render(request, 'polls/results.html', context)
