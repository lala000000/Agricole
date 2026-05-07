# Projet d’études B2 — Application de suivi agricole

## Contexte

Nous avons développé une application permettant d’aider les agriculteurs à suivre leurs cultures et leurs parcelles, en centralisant les données et en facilitant leur analyse.

---

## Objectif

Nous proposons une application web permettant :

- la gestion des parcelles agricoles
- l’ajout d’observations terrain  
- la visualisation des données  
- la détection de situations à risque  
- la visualisation des informations via un tableau de bord

Le projet vise la réalisation d’un MVP fonctionnel.
---

## Technologies utilisées

- Frontend : HTML / CSS  
- Backend : Django (framework backend utilisé pour gérer la logique serveur)  
- Base de données : SQLite (base de données légère utilisée pour stocker les données)
- Déploiement : Machine virtuelle  
- Gestion de version : GitHub  

---

## Fonctionnalités

### 1 Gestion des parcelles
- Création de parcelles
- Modification et suppression
- Visualisation des données associées

### 2 Gestion des cultures
- Association culture / parcelle
- Suivi de l’évolution des cultures

### 3 Observations terrain
- Ajout de données (température, humidité, état du sol…)
- Historique des observations

### 4 Tableau de bord
- Vue globale des données
- Synthèse des informations importantes
- Affichage des alertes

### 5 Système d’alertes
Le système analyse les données selon des règles métier simples.
---

## Exemple de règle métier

Si l’humidité est supérieure à 80% et la température supérieure à 20°C, une alerte de risque est affichée.

---

## Base de données

Les principales tables sont :

- Parcelles  
- Cultures  
- Observations  
- Météo  
- Alertes  


Modélisation : 
- MCD réalisé 
- MLD réalisé 

Le projet repose sur un jeu de données fourni par l’école, ces données ont été conçues pour simuler un environnement agricole réaliste et permettent de tester l’ensemble des fonctionnalités de l’application (gestion des parcelles, observations, alertes et visualisation).

Le système ne repose pas sur des données en temps réel dans cette version du MVP.

---

## Démonstration

L’application permet de :

- consulter le tableau de bord déjà alimenté en données  
- visualiser les informations existantes  
- ajouter de nouvelles parcelles  
- ajouter des observations supplémentaires  

Le projet fonctionne avec des données simulées ou saisies manuellement.

---

## Architecture

Utilisateur → Frontend → Backend (Django) → Base de données (SQLite)

---

## Installation

git clone <repo>
cd projet

python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux / Mac

pip install -r requirements.txt
python manage.py runserver