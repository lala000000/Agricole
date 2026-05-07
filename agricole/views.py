import datetime
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
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
  context = {
    'nbralerte': get_alertes_count(),
    'cultures': cultures,
  }
  return HttpResponse(template.render(context, request))

def culture(request, id):
  culture = get_object_or_404(Culture.objects.select_related('parcelle'), id=id)
  template = loader.get_template('culture.html')
  context = {
    'nbralerte': get_alertes_count(),
    'culture': culture,
  }
  return HttpResponse(template.render(context, request))

def create_culture(request):
  if request.method == 'POST':
    type_culture = request.POST.get('type')
    date_semis = request.POST.get('date_semis')
    parcelle_id = request.POST.get('parcelle')
    parcelle = get_object_or_404(Parcelle, id=parcelle_id)
    Culture.objects.create(
      type=type_culture,
      date_semis=date_semis,
      parcelle=parcelle,
    )
    return redirect('cultures')

  template = loader.get_template('create_culture.html')
  context = {
    'nbralerte': get_alertes_count(),
    'parcelles': Parcelle.objects.all(),
  }
  return HttpResponse(template.render(context, request))

def edit_culture(request, id):
  culture = get_object_or_404(Culture.objects.select_related('parcelle'), id=id)

  if request.method == 'POST':
    culture.type = request.POST.get('type')
    culture.date_semis = request.POST.get('date_semis')
    parcelle_id = request.POST.get('parcelle')
    culture.parcelle = Parcelle.objects.get(id=parcelle_id)
    culture.save()
    return redirect('cultures')

  template = loader.get_template('edit_culture.html')
  context = {
    'nbralerte': get_alertes_count(),
    'culture': culture,
    'parcelles': Parcelle.objects.all(),
  }
  return HttpResponse(template.render(context, request))

def delete_culture(request, id):
  culture = get_object_or_404(Culture, id=id)

  if request.method == 'POST':
    culture.delete()
    return redirect('cultures')

  return redirect('cultures')

def alertes(request):
  template = loader.get_template('alertes.html')
  context = {
    'nbralerte' : get_alertes_count()
  }
  return HttpResponse(template.render(context, request))

def observations(request):
  allobservations = Observation.objects.all().order_by('-date')[:10]
  template = loader.get_template('observations.html')
  context = {
    'nbralerte': get_alertes_count(),
    'observations': allobservations,
    'parcelles': Parcelle.objects.all(),
  }
  return HttpResponse(template.render(context, request))

def add_observation(request):
  if request.method == 'POST':
    parcelle_id = request.POST.get('parcel')
    etat = request.POST.get('etat')
    commentaire = request.POST.get('comment')
    
    parcelle = Parcelle.objects.get(id=parcelle_id)
    Observation.objects.create(
      parcelle=parcelle,
      etat=etat,
      commentaire=commentaire,
      date=datetime.date.today()
    )
    return redirect('observations')
  
  return redirect('observations')

def parcel(request, id):
  parcelle = get_object_or_404(
    Parcelle.objects.prefetch_related('cultures', 'observations', 'alertes'),
    id=id
  )
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
  if request.method == 'POST':
    nom = request.POST.get('nom')
    localisation = request.POST.get('localisation')
    surface_ha = request.POST.get('surface_ha')

    Parcelle.objects.create(
      nom=nom,
      localisation=localisation,
      surface_ha=float(surface_ha) if surface_ha else 0,
    )
    return redirect('parcels')

  template = loader.get_template('create_parcelle.html')
  context = {
    'nbralerte': get_alertes_count(),
  }
  return HttpResponse(template.render(context, request))

def edit_parcelle(request, id):
  parcelle = get_object_or_404(Parcelle, id=id)

  if request.method == 'POST':
    parcelle.nom = request.POST.get('nom')
    parcelle.localisation = request.POST.get('localisation')
    surface_ha = request.POST.get('surface_ha')
    parcelle.surface_ha = float(surface_ha) if surface_ha else 0
    parcelle.save()
    return redirect('parcels')

  template = loader.get_template('edit_parcelle.html')
  context = {
    'nbralerte': get_alertes_count(),
    'parcelle': parcelle,
  }
  return HttpResponse(template.render(context, request))

def delete_parcelle(request, id):
  parcelle = get_object_or_404(Parcelle, id=id)

  if request.method == 'POST':
    parcelle.delete()
    return redirect('parcels')

  return redirect('parcels')

def profile(request):
  template = loader.get_template('profile.html')
  context = {
    'nbralerte' : get_alertes_count(),
    'user': request.user,
  }
  return HttpResponse(template.render(context, request))

def edit_profile(request):
  user = request.user

  if request.method == 'POST':
    user.username = request.POST.get('username')
    user.email = request.POST.get('email')
    user.save()
    return redirect('profile')

  template = loader.get_template('edit_profile.html')
  context = {
    'nbralerte': get_alertes_count(),
    'user': user,
  }
  return HttpResponse(template.render(context, request))

def settings(request):
  template = loader.get_template('settings.html')
  context = {
    'nbralerte' : get_alertes_count()
  }
  return HttpResponse(template.render(context, request))