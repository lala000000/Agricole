from django.db import models

class Parcelle(models.Model):
    nom = models.CharField(max_length=255)
    localisation = models.CharField(max_length=255)
    surface_ha = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['nom']


class Plante(models.Model):
    TYPES = [
        ('Blé', 'Blé'),
        ('Maïs', 'Maïs'),
        ('Orge', 'Orge'),
        ('Tournesol', 'Tournesol'),
        ('Colza', 'Colza'),
    ]
    
    nom = models.CharField(max_length=255, unique=True, choices=TYPES)
    
    # Température Stress hydrique (°C)
    temp_stress_faible_min = models.FloatField(null=True, blank=True)
    temp_stress_faible_max = models.FloatField(null=True, blank=True)
    temp_stress_moyen_min = models.FloatField(null=True, blank=True)
    temp_stress_moyen_max = models.FloatField(null=True, blank=True)
    temp_stress_eleve_min = models.FloatField(null=True, blank=True)
    temp_stress_eleve_max = models.FloatField(null=True, blank=True)
    
    # Humidité Stress hydrique (%)
    humidite_stress_faible_min = models.IntegerField(null=True, blank=True)
    humidite_stress_faible_max = models.IntegerField(null=True, blank=True)
    humidite_stress_moyen_min = models.IntegerField(null=True, blank=True)
    humidite_stress_moyen_max = models.IntegerField(null=True, blank=True)
    humidite_stress_eleve_min = models.IntegerField(null=True, blank=True)
    humidite_stress_eleve_max = models.IntegerField(null=True, blank=True)
    
    # Pluie Stress hydrique (mm/jour)
    pluie_stress_faible_min = models.FloatField(null=True, blank=True)
    pluie_stress_faible_max = models.FloatField(null=True, blank=True)
    pluie_stress_moyen_min = models.FloatField(null=True, blank=True)
    pluie_stress_moyen_max = models.FloatField(null=True, blank=True)
    pluie_stress_eleve_min = models.FloatField(null=True, blank=True)
    pluie_stress_eleve_max = models.FloatField(null=True, blank=True)
    
    # Température Risque maladie (°C)
    temp_maladie_faible_min = models.FloatField(null=True, blank=True)
    temp_maladie_faible_max = models.FloatField(null=True, blank=True)
    temp_maladie_moyen_min = models.FloatField(null=True, blank=True)
    temp_maladie_moyen_max = models.FloatField(null=True, blank=True)
    temp_maladie_eleve_min = models.FloatField(null=True, blank=True)
    temp_maladie_eleve_max = models.FloatField(null=True, blank=True)
    
    # Humidité Risque maladie (%)
    humidite_maladie_faible_min = models.IntegerField(null=True, blank=True)
    humidite_maladie_faible_max = models.IntegerField(null=True, blank=True)
    humidite_maladie_moyen_min = models.IntegerField(null=True, blank=True)
    humidite_maladie_moyen_max = models.IntegerField(null=True, blank=True)
    humidite_maladie_eleve_min = models.IntegerField(null=True, blank=True)
    humidite_maladie_eleve_max = models.IntegerField(null=True, blank=True)
    
    # Pluie Risque maladie (mm/jour)
    pluie_maladie_faible_min = models.FloatField(null=True, blank=True)
    pluie_maladie_faible_max = models.FloatField(null=True, blank=True)
    pluie_maladie_moyen_min = models.FloatField(null=True, blank=True)
    pluie_maladie_moyen_max = models.FloatField(null=True, blank=True)
    pluie_maladie_eleve_min = models.FloatField(null=True, blank=True)
    pluie_maladie_eleve_max = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return self.nom
    
    class Meta:
        ordering = ['nom']


class Culture(models.Model):
    plante = models.ForeignKey(Plante, on_delete=models.CASCADE, related_name='cultures')
    date_semis = models.DateField()
    parcelle = models.ForeignKey(Parcelle, on_delete=models.CASCADE, related_name='cultures')

    def __str__(self):
        return f"{self.plante.nom} - {self.parcelle.nom}"
    
    class Meta:
        ordering = ['-date_semis']


class Observation(models.Model):
    ETATS = [
        ('OK', 'OK'),
        ('Stress hydrique', 'Stress hydrique'),
        ('Maladie détectée', 'Maladie détectée'),
        ('Risque maladie', 'Risque maladie'),
    ]
    date = models.DateField()
    etat = models.CharField(max_length=255, choices=ETATS)
    commentaire = models.CharField(max_length=255, blank=True, null=True)
    parcelle = models.ForeignKey(Parcelle, on_delete=models.CASCADE, related_name='observations')

    def __str__(self):
        return f"{self.parcelle.nom} - {self.commentaire} - {self.date}"

    class Meta:
        ordering = ['-date']


class Meteo(models.Model):
    date = models.DateField(unique=True)
    temperature = models.IntegerField()
    humidite = models.IntegerField()
    pluie_mm = models.IntegerField()

    def __str__(self):
        return f"Météo {self.temperature}°C / {self.humidite}% / {self.pluie_mm}mm de précipitation"

    class Meta:
        ordering = ['-date']


class Alerte(models.Model):
    NIVEAUX = [
        (1, 'Faible'),
        (2, 'Moyen'),
        (3, 'Élevé'),
    ]
    date = models.DateField()
    type = models.CharField(max_length=255)
    niveau = models.IntegerField(choices=NIVEAUX)
    parcelle = models.ForeignKey(Parcelle, on_delete=models.CASCADE, related_name='alertes')
    est_lue = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.type} - {self.parcelle.nom}"

    class Meta:
        ordering = ['-date']