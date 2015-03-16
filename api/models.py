from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
  """
  """
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  name = models.CharField(max_length=40)
  user = models.ForeignKey(User)

  def __str__(self):
    return self.name

class TimeChunk(models.Model):
  """
  """
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  date = models.DateField(auto_now_add=True)
  minutes = models.IntegerField(default=0)
  skill = models.ForeignKey(Skill)

