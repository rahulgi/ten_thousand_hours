from api.models import Skill
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET', 'POST'])
def skills(request):
  """
  """
  if request.method == 'GET':
    return HttpResponse(serializers.serialize('json', Skill.objects.all()),
                        content_type='application/json')
  else:
    pass
