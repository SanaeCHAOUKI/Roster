# Roster – Application de Gestion des Ressources Humaines

Roster est une application web Django développée dans le cadre d'un Projet de Fin d'Études. Elle permet aux responsables RH de gérer les employés, les congés, la paie et de prédire les risques de départ grâce à un modèle de Machine Learning.

---

## Prérequis

- Python 3.10 ou supérieur
- pip



## Installation

Clonez ou extrayez le projet, puis placez-vous dans le dossier :

```bash
cd rh_app
```

Créez et activez un environnement virtuel :

```bash
python -m venv venv
venv\Scripts\activate
```

Installez les dépendances :

```bash
pip install -r requirements.txt
```

Appliquez les migrations :

```bash
python manage.py makemigrations
python manage.py migrate
```

Chargez des données de démonstration :

```bash
python seed_data.py
```

Lancez le serveur :

```bash
python manage.py runserver
```

L'application est accessible sur http://127.0.0.1:8000/



## Connexion

| Profil  | Rôle                        |
|---------|-----------------------------|
| Admin   | Gestion complète du système |
| RH      | Gestion RH et prédictions   |
| Employé | Espace personnel            |

Identifiants par défaut : `admin` / `admin123`



## Fonctionnalités

- Tableau de bord avec statistiques et graphiques
- Gestion des employés (ajout, modification, suppression, recherche)
- Gestion des congés (demandes, validation, suivi)
- Gestion de la paie (bulletins détaillés)
- Prédiction du risque de départ via régression logistique
- Gestion des modèles de Machine Learning



## Technologies

- Python, Django 4.2, SQLite
- HTML, CSS, JavaScript, Chart.js
- Scikit-learn, Joblib


## Structure

rh_app/
├── rh_app/
├── employees/
├── templates/
├── static/
├── ml_models/
├── seed_data.py
├── requirements.txt
└── manage.py


Projet réalisé par CHAOUKI Sanae, BERKI Khadija et ALLAOUI Fayrouz — EST Oujda, 2025/2026.