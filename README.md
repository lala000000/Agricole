# Projet d’études B2 — Application de suivi agricole


## Contexte

Dans un contexte de transformation numérique du secteur agricole, les acteurs du domaine ont besoin d’outils leur permettant de mieux suivre leurs cultures, d’exploiter des données (météo, observations terrain, parcelles) et d’améliorer leur prise de décision.

Les informations agricoles étant souvent dispersées et difficiles à exploiter, il devient nécessaire de proposer une solution numérique centralisée permettant de les structurer, les visualiser et les analyser simplement.

## Problématique

**Comment une application web peut-elle aider les agriculteurs à suivre leurs cultures et à améliorer leur prise de décision ?**

## Objectif

Nous proposons une application web permettant :

- la gestion des parcelles agricoles
- l’ajout d’observations terrain  
- la visualisation des données  
- la détection de situations à risque  
- la visualisation des informations via un tableau de bord

Le projet vise la réalisation d’un MVP fonctionnel.


## Technologies utilisées

- Frontend : HTML / CSS  
- Backend : Django (framework backend utilisé pour gérer la logique serveur)  
- Base de données : SQLite (base de données légère utilisée pour stocker les données)
- Déploiement : Machine virtuelle  
- Gestion de version : GitHub   


### Justification des choix techniques

| Technologie | Choix | Justification |
|---|---|---|
| Frontend | HTML / CSS | Création d’une interface simple, légère et adaptée au MVP |
| Backend | Django (Python) | Framework structuré permettant un développement rapide et une gestion simplifiée de la logique métier |
| Base de données | SQLite | Solution légère et facile à intégrer avec Django |
| Déploiement | Machine virtuelle | Permet de simuler un environnement serveur et d’isoler le projet |
| Gestion de version | GitHub | Suivi du développement, gestion des versions et travail collaboratif |


## Fonctionnalités

L’application permet de gérer et d’analyser les données agricoles à travers plusieurs modules fonctionnels.

#### 1. Gestion des parcelles
- Création, modification et suppression de parcelles agricoles
- Consultation des informations détaillées
- Suivi des caractéristiques de chaque parcelle

---

#### 2. Gestion des cultures
- Association des cultures aux parcelles
- Suivi de l’évolution des cultures dans le temps
- Organisation des données par type de culture

---

#### 3. Observations terrain
- Enregistrement des données terrain (température, humidité, état du sol…)
- Historique des observations pour chaque parcelle
- Suivi de l’évolution des conditions agricoles

---

#### 4. Tableau de bord
- Visualisation globale des données agricoles
- Synthèse des indicateurs clés
- Mise en évidence des informations importantes
- Accès rapide aux alertes du système

---

#### 5. Système d’alertes
Le système analyse les données à partir de règles métier simples afin d’identifier des situations à risque.

*Exemple de règle métier : Si l’humidité est supérieure à 80% et la température supérieure à 20°C, une alerte de risque est affichée.*


## Base de données

### Modélisation :  

#### 1. MCD (Modèle Conceptuel de Données)

Le MCD représente les entités principales du système et leurs relations :

- Parcelle
- Culture
- Observation
- Météo
- Alerte

Relations principales :
- Une parcelle possède plusieurs observations
- Une culture est associée à une parcelle
- Une alerte est générée à partir d’une observation

---

#### 2. MLD (Modèle Logique de Données)


Le MLD représente l’organisation des tables, des champs et des relations utilisées dans la base de données.

Le schéma complet du MLD est disponible dans les annexes du projet.

---

Le projet utilise un jeu de données fourni par l’école afin de simuler un environnement agricole réaliste.

Ces données permettent de tester les principales fonctionnalités de l’application :
- gestion des parcelles
- suivi des cultures
- observations terrain
- système d’alertes
- visualisation des données

Cette version correspond à un MVP et ne repose pas sur des données en temps réel.

---

## Démonstration

L’utilisateur peut :

- consulter un tableau de bord des données agricoles
- créer et gérer des parcelles
- ajouter des observations terrain
- visualiser les alertes générées automatiquement

---

## Architecture



---

## Installation

#### Prérequis

Avant de lancer le projet, les éléments suivants doivent être installés :

- Python 3.10 ou supérieur
- pip
- Git
- Visual Studio Code (recommandé)

---

##### 1. Cloner le projet

```bash
git clone <URL_DU_REPO>
cd projet-agricole
```

---

##### 2. Créer un environnement virtuel

```bash
python -m venv venv
```

---

##### 3. Activer l’environnement virtuel

###### Windows
```bash
venv\Scripts\activate
```

###### Linux / Mac
```bash
source venv/bin/activate
```

---

##### 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

##### 5. Appliquer les migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

##### 6. Lancer le serveur Django

```bash
python manage.py runserver
```

---

##### 7. Accéder à l’application

Ouvrir le navigateur à l’adresse suivante :

```text
http://127.0.0.1:8000
```

--- 
## Conclusion

Ce projet répond à une problématique réelle du secteur agricole en proposant une solution de suivi et d’analyse des cultures.

Il permet de centraliser les données, de les structurer et de les exploiter via des règles métier simples afin d’améliorer la prise de décision.