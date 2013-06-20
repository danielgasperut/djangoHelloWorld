from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from polls.models import Poll, Choice

def index(request):
  #return HttpResponse("Hello World. You're at the poll index")
  latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
  template = loader.get_template('polls/index.html')
  context = Context ({
    'latest_poll_list': latest_poll_list,
    })
  return HttpResponse(template.render(context))

def detail(request, poll_id):
  try:
    poll = Poll.objects.get(pk=poll_id)
  except Poll.DoesNotExist:
    raise Http404
  return render(request,'polls/detail.html',{'poll':poll})
  #return HttpResponse("You're looking at poll %s" % poll_id)

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

def results(request, poll_id):
  try:
    poll = Poll.objects.get(pk=poll_id)
  except Poll.DoesNotExist:
    raise Http404
  return render(request,'polls/results.html',{'poll':poll})
  #return render(request, reverse('polls:results' , args=(poll.id,)), {'poll':poll})

  #return HttpResponse("You're looking at poll %s" % poll_id)

def model(request):
  template = loader.get_template('polls/model.html')
  context = Context ({})
  return HttpResponse(template.render(context))

