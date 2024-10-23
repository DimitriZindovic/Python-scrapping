# Projet Scraping Python

### Rendu de cours Python

## Description :

Le projet consiste à récupérer des informations sur ce site [Books to Scrape](https://books.toscrape.com/index.html) et à stocker les données dans des fichiers CSV.

### Installation du projet :

#### _Création de l'environnement virtuel_

Pour Windows :

```bash
python -m venv env
```

Pour macOS :

```bash
python3 -m venv env
```

#### _Activation de l'environnement_

Pour Windows :

```bash
env\Scripts\activate
```

Pour macOS :

```bash
source env/bin/activate
```

#### _Installation des modules_

```bash
pip install -r requirements.txt
```

### Phases du projet :

#### **Phase 1** :

- Récupération de l'URL de la page d'un livre depuis la page d'accueil. Une fois l'URL dédiée obtenue, les informations du livre sont collectées et enregistrées dans un fichier CSV nommé `book.csv`.

Lancer :

```bash
python step1.py
```

#### **Phase 2** :

- Refactorisation du code en créant des fonctions pour éviter la duplication de lignes. Récupération de l'URL d'une catégorie, puis scraping des données de tous les livres de cette catégorie. Si la catégorie comporte plusieurs pages, passage automatique à la page suivante après avoir scrappé tous les livres de la page actuelle.

Lancer :

```bash
python step2.py
```

#### **Phase 3** :

- Téléchargement des images des livres consultés sur le site et stockage dans le dossier `images`. Chaque image est renommée avec le nom du livre correspondant.

Lancer :

```bash
python step2.py
```

#### **Phase 4** :

- Bouclage sur toutes les catégories du site pour récupérer les livres. Création d'un fichier CSV pour chaque catégorie (nommé selon la catégorie) et d'un dossier pour stocker les images des livres correspondants. Toutes les données des livres sont enregistrées dans le fichier CSV associé.

Lancer :

```bash
python step4.py
```

## Technologies :

- Python

## Auteur :

Dimitri Zindovic
