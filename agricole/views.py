from django.http import HttpResponse
from django.template import loader
from .models import Culture

def dashboard(request):
  template = loader.get_template('dashboard.html')
  return HttpResponse(template.render())

def cultures(request):
  template = loader.get_template('cultures.html')
  cultures = Culture.objects.select_related('parcelle').all()
  return HttpResponse(template.render({'cultures': cultures}))

def alertes(request):
  template = loader.get_template('alertes.html')
  return HttpResponse(template.render())

def observations(request):
  template = loader.get_template('observations.html')
  return HttpResponse(template.render())

def parcel(request):
  template = loader.get_template('parcel.html')
  return HttpResponse(template.render())

def parcels(request):
  template = loader.get_template('parcels.html')
  return HttpResponse(template.render())

def profile(request):
  template = loader.get_template('profile.html')
  return HttpResponse(template.render())

def settings(request):
  template = loader.get_template('settings.html')
  return HttpResponse(template.render())