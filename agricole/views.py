import datetime
from django.http import HttpResponse
from django.template import loader
from .models import Meteo, Observation, Parcelle, Alerte

def dashboard(request):
  allparcelles = Parcelle.objects.all()
  allobservations = Observation.objects.all()
  allalertes = Alerte.objects.all()
  today = datetime.date.today()
  compteurparcelle = 0
  compteurobservation = 0
  compteuralerte = 0
  alerteniveaumoyenne = 0
  
  jourmeteo = Meteo.objects.filter(date=today).first()

  for i in allparcelles:
    compteurparcelle += 1

  for i in allobservations:
    if i.date  > today - datetime.timedelta(days=14):
      compteurobservation += 1
  
  for i in allalertes:
    if i.est_lue == 0:
      compteuralerte += 1
      alerteniveaumoyenne += i.niveau
  
  alerteniveaumoyenne = round(alerteniveaumoyenne / compteuralerte)
  niveau_label = dict(Alerte.NIVEAUX).get(alerteniveaumoyenne, 'Inconnu')
  
  observations_risque = Observation.objects.filter(
    etat__in=['Stress hydrique', 'Maladie détectée', 'Risque maladie']
  ).order_by('-date')[:3]
  
  template = loader.get_template('dashboard.html')
  context = {
    'meteo' : jourmeteo,
    'nbrparcelle' : compteurparcelle,
    'nbrobservation' : compteurobservation,
    'nbralerte' : compteuralerte,
    'niveaualerte' : niveau_label,
    'observations_risque' : observations_risque
  }
  return HttpResponse(template.render(context, request))

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