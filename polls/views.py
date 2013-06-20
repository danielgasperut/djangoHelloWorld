from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Poll, Choice

class IndexView(generic.ListView):
  template_name = 'polls/index.html'
  #context_object_name = 'latest_poll_list'
  
  def get_queryset(self):
    return Poll.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
  template_name = 'polls/detail.html'
  model = Poll

class ResultsView(generic.DetailView):
  model = Poll
  template_name = 'polls/results.html'

def vote(request, poll_id):
  p = get_object_or_404(Poll, pk=poll_id)
  try:
    selected_choice = p.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    #redisplay the form
    return render(request, 'polls/detail.html', {
      'poll':p,
      'error_message': "You Didn't select a choice.",
      })
  else:
    selected_choice.votes += 1
    selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))

  #return HttpResponse("You're looking at poll %s" % poll_id)

def model(request):
  template = loader.get_template('polls/model.html')
  context = Context ({})
  return HttpResponse(template.render(context))

