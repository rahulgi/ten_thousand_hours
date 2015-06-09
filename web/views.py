import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.timezone import utc
from django.views.decorators.http import require_http_methods

from api.models import Skill, TimeChunk

@require_http_methods(['POST'])
def add_skill_time(request, pk):
  skill = get_object_or_404(Skill, pk=pk)
  now = datetime.date.today()
  time_chunk, created = TimeChunk.objects.get_or_create(date=now, skill=skill)
  try:
    time_chunk.minutes = time_chunk.minutes + int(request.POST['minutes'])
  except:
    return HttpResponseBadRequest(request)
  time_chunk.save()
  return redirect('/skills/%s/' % pk)

@require_http_methods(['POST'])
def create_skill(request):
  #Need User object of requestor
  user = request.user
  skill = Skill.objects.create(name=request.POST['name'],
                               user=user)
  return redirect('/')

@require_http_methods(['GET'])
def index(request):
  skills = Skill.objects.all().filter(user_id=request.user.id)
  return render(request, 'index.html', {
    'skills': skills,
  })

@require_http_methods(['GET'])
def skill(request, pk):
  skill = get_object_or_404(Skill, pk=pk)
  time_chunks = skill.timechunk_set.all()
  sum_total_minutes = 0
  for chunk in time_chunks:
    sum_total_minutes += chunk.minutes
  return render(request, 'skill.html', {
      'skill': skill,
      'sum_total_minutes': sum_total_minutes,
  })

@require_http_methods(['GET', 'POST'])
def register(request):
  if request.method == 'GET':
    form = UserCreationForm()
    return render(request, 'register.html', {
      'form': form,
    })
  else:
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      authenticated_user = authenticate(
        username=user.username, 
        password=form.cleaned_data.get('password1'))
      login(request, authenticated_user)
      return redirect('/')
    else:
      return render(request, 'register.html', {
        'form': form,
      })

def logout_view(request):
  logout(request)
  return redirect('/')

