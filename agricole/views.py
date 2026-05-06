import datetime
from django.http import HttpResponse
from django.template import loader
from .models import Meteo, Observation, Parcelle, Alerte, Culture

def get_alertes_count():
  """Retourne le nombre d'alertes non lues"""
  return Alerte.objects.filter(est_lue=False).count()

def dashboard(request):
  allparcelles = Parcelle.objects.all()
  allobservations = Observation.objects.all()
  allalertes = Alerte.objects.filter(est_lue=False)
  today = datetime.date.today()
  compteurparcelle = 0
  compteurobservation = 0
  compteuralerte = 0
  alerteniveaumoyenne = 0
  
  jourmeteo = Meteo.objects.filter(date=today).first()

  for i in allparcelles:
    compteurparcelle += 1

  for i in allobservations:
    if i.date > today - datetime.timedelta(days=14):
      compteurobservation += 1
  
  for i in allalertes:
    compteuralerte += 1
    alerteniveaumoyenne += i.niveau
  
  if compteuralerte > 0:
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

def cultures(request):
  template = loader.get_template('cultures.html')
  cultures = Culture.objects.select_related('parcelle').all()
  return HttpResponse(template.render({'cultures': cultures}))

def alertes(request):
  template = loader.get_template('alertes.html')
  context = {
    'nbralerte' : get_alertes_count()
  }
  return HttpResponse(template.render(context, request))

def observations(request):
  template = loader.get_template('observations.html')
  context = {
    'nbralerte' : get_alertes_count()
  }
  return HttpResponse(template.render(context, request))

def parcel(request, id):
  parcelle = Parcelle.objects.prefetch_related('cultures', 'observations', 'alertes').get(id=id)
  template = loader.get_template('parcel.html')
  context = {
    'nbralerte': get_alertes_count(),
    'parcelle': parcelle,
  }
  return HttpResponse(template.render(context, request))

def parcels(request):
  parcelles = Parcelle.objects.prefetch_related('cultures', 'observations').all()
  template = loader.get_template('parcels.html')
  context = {
    'nbralerte': get_alertes_count(),
    'parcelles': parcelles,
  }
  return HttpResponse(template.render(context, request))

def create_parcelle(request):
  template = loader.get_template('create_parcelle.html')
  context = {
    'nbralerte': get_alertes_count(),
  }
  return HttpResponse(template.render(context, request))

def edit_parcelle(request, id):
  parcelle = Parcelle.objects.get(id=id)
  template = loader.get_template('edit_parcelle.html')
  context = {
    'nbralerte': get_alertes_count(),
    'parcelle': parcelle,
  }
  return HttpResponse(template.render(context, request))

def profile(request):
  template = loader.get_template('profile.html')
  context = {
    'nbralerte' : get_alertes_count()
  }
  return HttpResponse(template.render(context, request))

def settings(request):
  template = loader.get_template('settings.html')
  context = {
    'nbralerte' : get_alertes_count()
  }
  return HttpResponse(template.render(context, request))