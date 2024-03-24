from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.shortcuts import redirect

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

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'voted_polls' in request.session:
            if str(self.object.id) in request.session['voted_polls']:
                return redirect('polls:results', slug=self.object.slug)
        return super().get(request, *args, **kwargs)


class ResultsDeteilView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_can_see_results = False
        if 'voted_polls' in self.request.session:
            print("In ResultsDeteilView: ", self.request.session['voted_polls'])  # Debugging-Ausgabe
            if str(self.object.id) in self.request.session['voted_polls']:  # Überprüfung anpassen
                user_can_see_results = True
        context['access'] = user_can_see_results
        return context


def vote(request, slug):
    umfrage = get_object_or_404(Poll, slug=slug)
    try:
        ausgewahlte_antwort = umfrage.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return HttpResponse("Fehler: Keine Antwort ausgewählt.")
    else:
        ausgewahlte_antwort.votes += 1
        ausgewahlte_antwort.save()
        if 'voted_polls' in request.session:
            print("Vor dem Hinzufügen: ", request.session['voted_polls'])  # Debugging-Ausgabe
            if type(request.session['voted_polls']) != list:
                request.session['voted_polls'].append(str(umfrage.id))  # umfrage.id in einen String umwandeln
            else:
                request.session['voted_polls'] = [str(umfrage.id)]  # umfrage.id in einen String umwandeln
            print("Nach dem Hinzufügen: ", request.session['voted_polls'])  # Debugging-Ausgabe
        else:
            request.session['voted_polls'] = [str(umfrage.id)]  # umfrage.id in einen String umwandeln
        return HttpResponseRedirect(reverse('polls:results', args=(umfrage.slug,)))
