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

Le MLD représente l’organisation des tables et des relations de la base de données.

Le projet utilise un jeu de données fourni par l’école afin de simuler un environnement agricole réaliste et tester les fonctionnalités de l’application.

Cette version correspond à un MVP et ne repose pas sur des données en temps réel.


## Démonstration

L’utilisateur peut interagir avec l’application de la manière suivante :

- accéder au tableau de bord pour consulter les données agricoles
- créer et gérer des parcelles
- ajouter des observations terrain
- visualiser automatiquement les alertes générées par le système

---
*Exemple de scénario utilisateur :*

| Étape | Ce que fait l’utilisateur | Ce que l’application fait |
|---|---|---|
| 1 | Il ouvre une parcelle (ex : Parcelle 3) | L’application affiche les informations de la parcelle |
| 2 | Il regarde l’état des cultures | Il voit par exemple : sol sec, feuilles jaunies |
| 3 | Il ajoute une observation terrain | L’information est enregistrée dans la base de données |
| 4 | L’application analyse les données | Elle détecte un risque (ex : maladie possible) |
| 5 | Une alerte apparaît | L’utilisateur est informé qu’il faut agir |

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
git clone https://github.com/lala000000/Agricole.git
cd Agricole
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

## Limites et améliorations

Ce MVP constitue une première version fonctionnelle de l’application.

Certaines améliorations possibles :

- intégration de données météo en temps réel
- ajout de graphiques d’évolution des cultures
- mise en place d’un système d’intelligence prédictive
- déploiement cloud pour un usage à grande échelle


## Conclusion

Ce projet nous a permis de concevoir une application de suivi agricole répondant à un besoin concret, centraliser et rendre exploitables des données liées aux parcelles et aux cultures.

L’application facilite le suivi des informations agricoles et aide à identifier certaines situations à risque grâce à des règles métier simples.

Ce travail constitue une première version fonctionnelle (MVP) qui pourrait être améliorée par la suite avec l’ajout de données en temps réel, de visualisations plus avancées et un déploiement sur une infrastructure cloud.
