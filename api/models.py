from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
  """
  """
  name = models.CharField(max_length=40)
  time = models.PositiveIntegerField(default=0)
  user = models.ForeignKey(User)
