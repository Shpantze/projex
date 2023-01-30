import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.
class CustUser(AbstractUser):
  pass

class TopLid(models.Model):
  item = models.TextField()
  made = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.item
    
  class Meta:
    db_table = 'toplid'