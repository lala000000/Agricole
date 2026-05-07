from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from agricole.models import Alerte, Culture, Meteo, Plante

class Command(BaseCommand):
    help = "Génère automatiquement les alertes basées sur les seuils de plantes et données météo"

    def add_arguments(self, parser):
        parser.add_argument('--days', type=int, default=7)
        parser.add_argument('--force', action='store_true')

    def handle(self, *args, **options):
        days = options['days']
        force = options['force']
        date_debut = datetime.now().date() - timedelta(days=days)
        
        if force:
            Alerte.objects.filter(date__gte=date_debut).delete()

        alertes_created = 0
        meteos = Meteo.objects.filter(date__gte=date_debut)
        
        for culture in Culture.objects.select_related('plante', 'parcelle'):
            for meteo in meteos:
                for alerte_type, checker in [
                    ('Stress hydrique', self._check_stress),
                    ('Risque maladie', self._check_maladie),
                ]:
                    niveau = checker(culture.plante, meteo)
                    if niveau:
                        _, created = Alerte.objects.get_or_create(
                            date=meteo.date,
                            type=alerte_type,
                            parcelle=culture.parcelle,
                            defaults={'niveau': niveau}
                        )
                        if created:
                            alertes_created += 1

        self.stdout.write(self.style.SUCCESS(f"✓ {alertes_created} alerte(s)."))

    def _check_stress(self, plante, meteo):
        return self._get_niveau(
            meteo.temperature,
            meteo.humidite,
            meteo.pluie_mm,
            plante.temp_stress_faible_min, plante.temp_stress_faible_max,
            plante.humidite_stress_faible_min, plante.humidite_stress_faible_max,
            plante.pluie_stress_faible_min, plante.pluie_stress_faible_max,
            plante.temp_stress_moyen_min, plante.temp_stress_moyen_max,
            plante.humidite_stress_moyen_min, plante.humidite_stress_moyen_max,
            plante.pluie_stress_moyen_min, plante.pluie_stress_moyen_max,
            plante.temp_stress_eleve_min, plante.temp_stress_eleve_max,
            plante.humidite_stress_eleve_min, plante.humidite_stress_eleve_max,
            plante.pluie_stress_eleve_min, plante.pluie_stress_eleve_max,
        )

    def _check_maladie(self, plante, meteo):
        return self._get_niveau(
            meteo.temperature,
            meteo.humidite,
            meteo.pluie_mm,
            plante.temp_maladie_faible_min, plante.temp_maladie_faible_max,
            plante.humidite_maladie_faible_min, plante.humidite_maladie_faible_max,
            plante.pluie_maladie_faible_min, plante.pluie_maladie_faible_max,
            plante.temp_maladie_moyen_min, plante.temp_maladie_moyen_max,
            plante.humidite_maladie_moyen_min, plante.humidite_maladie_moyen_max,
            plante.pluie_maladie_moyen_min, plante.pluie_maladie_moyen_max,
            plante.temp_maladie_eleve_min, plante.temp_maladie_eleve_max,
            plante.humidite_maladie_eleve_min, plante.humidite_maladie_eleve_max,
            plante.pluie_maladie_eleve_min, plante.pluie_maladie_eleve_max,
        )

    @staticmethod
    def _get_niveau(temp, humidite, pluie, *seuils):
        for niveau in [3, 2, 1]:
            idx = (niveau - 1) * 6
            t_min, t_max, h_min, h_max, p_min, p_max = seuils[idx:idx+6]
            if Command._in_range(temp, t_min, t_max) and \
               Command._in_range(humidite, h_min, h_max) and \
               Command._in_range(pluie, p_min, p_max):
                return niveau
        return None

    @staticmethod
    def _in_range(val, min_v, max_v):
        return val is not None and min_v is not None and max_v is not None and min_v <= val <= max_v