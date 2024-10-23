# Projet Scraping python

### Rendu de cours Python

## Description :

Le projet consiste a récupérer des informations sur ce site https://books.toscrape.com/index.html en mettant les informations dans des fichiers csv

**Installation du projet** :

**_Création de l'environnement virtuel_**

Pour Windows :

python -m venv env

Pour macOS :

python3 -m venv env

**_Activation de l'envrionnement_**

Pour Windows :

env\Scripts\activate

Pour macOS :

source env/bin/activate

**_Installation des modules_**

pip install -r requirements.txt

**Phase 1** :

- Récupération de l'URL de la page d'un livre depuis la page d'accueil. Une fois l'URL dédiée obtenue, je collecte toutes les informations nécessaires sur le livre. Ensuite, j'enregistre ces informations dans un fichier CSV nommé book.csv.

Lancer step1.py

**Phase 2** :

- Refactorisation du code en créant des fonctions pour éviter de dupliquer les mêmes lignes. Je récupère l'URL d'une catégorie, puis, une fois l'URL enregistrée, je scrappe les données de tous les livres de cette catégorie. Si la catégorie comporte plusieurs pages, je passe à la page suivante après avoir scrappé tous les livres de la page en cours.

Lancer step2.py

**Phase 3** :

- Ajout des images des livres consultés sur le site, en les téléchargeant directement dans le dossier images. Chaque image est renommée avec le nom du livre correspondant.

Lancer step2.py

**Phase 4** :

- On parcourt toutes les catégories du site pour récupérer les livres. Pour chaque catégorie, un fichier CSV est créé avec le nom de la catégorie, ainsi qu'un dossier pour stocker les images des livres de cette catégorie. Toutes les données des livres sont ensuite enregistrées dans le fichier CSV correspondant à la catégorie.

Lancer step4.py

## Technologies :

- Python

## Auteur :

Dimitri Zindovic
