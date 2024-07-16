from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import add_view

def home(request):
  all_rest = add_view.objects.all().values()
  template = loader.get_template('home.html')
  context = {
    'all_rest': all_rest ,
  }
  return HttpResponse(template.render(context, request))