from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Poll, Choice
from django.views import generic


def index(request):
    context = {
        'umfragen': Poll.objects.all(),
        'title': "Umfragen",
    }
    return render(request, 'polls/index.html', context)


class PollDeteilView(generic.DetailView):
    model = Poll
    template_name = 'polls/umfrage.html'


class ResultsDeteilView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'



def vote(request, slug):
    umfrage = get_object_or_404(Poll, slug=slug)
    try:
        ausgewahlte_antwort = umfrage.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return HttpResponse("Fehler: Keine Antwort ausgewählt.")
    else:
        ausgewahlte_antwort.votes += 1
        ausgewahlte_antwort.save()
        return HttpResponseRedirect('/abstimmung/' + slug + '/results/')
