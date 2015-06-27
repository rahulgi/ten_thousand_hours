from api.models import Skill
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET'])
def skills(request):
  """
  """
  if request.method == 'GET':
    return HttpResponse(serializers.serialize('json', Skill.objects.all()),
                        content_type='application/json')

@require_http_methods(['GET'])
def skill_times(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    return HttpResponse(serializers.serialize('json',
                        skill.timechunk_set.all()),
                        content_type='application/json')

