#import json
from http import HTTPStatus
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import TopLid
from django.core.files import File
from django.core import serializers
from django.template import loader
from django.views.decorators.cache import cache_control
from django.views.decorators.http import condition
# Create your views here.
def last_mod(request):
  #return str(TopLid.objects.all().earliest("-made"))
  return str(len(TopLid.objects.all()))
  
@cache_control(must_revalidate=True)
@condition(etag_func=last_mod)
def home(request):
  #item = TopLid.objects.filter(id__gt=0).values('item')
  #col = []
  #for i in item:
      #obj1 = obj(i)
      #col.append(obj1.elem)
  items = TopLid.objects.all()
  JsonSerial = serializers.get_serializer("json")
  j_seri = JsonSerial()
  with open('static/inapp/stuff.json', 'w') as f:
    j_seri.serialize(items, fields=("item"), indent=3, stream=f)
  #template = loader.get_template('inapp/index.html')
  #context = {'elem':col}
  #context = {'headers':request.headers}
  #response = HttpResponse(template.render(context))
  return render(request, 'inapp/index.html')

#class obj:
#  def __init__(self, elem):
#    self.elem = elem

def addItem(request):
  try:
    a = TopLid(item=request.POST['insert'])
    a.save()
  except:
    return HttpResponseRedirect(reverse('inapp:home'))
  else:
    return HttpResponseRedirect(reverse('inapp:home'))