from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import add_view
from .forms import AddForm

def home(request):
  all_rest = add_view.objects.all().values()
  template = loader.get_template('home.html')
  context = {
    'all_rest': all_rest ,
  }
  return HttpResponse(template.render(context, request))

def add_rest(request):
  template = loader.get_template('add_rest.html')
  if request.method == 'POST':
    form = AddForm(request.POST)
    if form.is_valid():
      rest_name = form.cleaned_data['rest_name']
      rest_spec = form.cleaned_data['rest_spec']
      rest_address = form.cleaned_data['rest_address']
      rest_webite = form.cleaned_data['rest_website']
      rest_phone = form.cleaned_data['rest_phone']
      form.save()
    return render(request, 'home.html')
  else:
    form = AddForm()
  return render(request, 'add_rest.html', {'form': form})