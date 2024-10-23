from bs4 import BeautifulSoup
import csv
import os
import requests

def scrap_page_book(url, csv_name):
    """
    Scrape les détails du livre depuis l'URL donnée et les écrit dans un fichier CSV.

    Args:
        url (str): L'URL de la page du livre à scraper.
        csv_name (str): Le nom du fichier CSV dans lequel écrire les détails du livre.
    """
    directory_name = "images"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    csv_exist = os.path.isfile(f'{csv_name}.csv')

    # Écrire l'en-tête dans le CSV s'il n'existe pas
    if not csv_exist:
        with open(f'{csv_name}.csv', mode='w', newline='', encoding="utf8") as file:
            writter = csv.writer(file)
            writter.writerow(['url_page_produit', 'code_produit_universel', 'titre', 'prix_avec_taxe', 'prix_sans_taxe', 'nombre_disponible', 'description_produit', 'catégorie', 'note_avis', 'url_image'])

    with open(f'{csv_name}.csv', mode='a', newline='', encoding="utf8") as fichier_csv:
        writter = csv.writer(fichier_csv)

        h1 = soup.find('h1')
        title = h1.text if h1 else 'N/A'

        p = soup.select('article.product_page > p')
        description = p[0].text if p else 'N/A'

        all_td = []
        table = soup.find('table')
        trs = table.find_all('tr')
        for tr in trs:
            td = tr.find('td').text
            all_td.append(td)

        upc = all_td[0]
        price_exact_tax = all_td[2]
        price_incl_tax = all_td[3]
        availability_not_clean = all_td[5]
        availability = ''.join([caractere for caractere in availability_not_clean if caractere.isdigit()])

        ul = soup.find('ul')
        a = ul.find_all('a')
        category = a[-1].text

        review_rating = soup.find('p', class_='star-rating')['class'][1]

        div = soup.find('div', class_='carousel-inner')
        image_search = soup.find('img')['src']
        image_url = image_search.replace('../../', 'https://books.toscrape.com/')

        # Créer le répertoire pour les images s'il n'existe pas
        if not os.path.exists(directory_name):
            os.mkdir(directory_name)

        # Enregistrer l'image dans le répertoire
        image_filename = os.path.join(directory_name, os.path.basename(image_url))
        response = requests.get(image_url)
        with open(image_filename, mode='wb') as file:
            file.write(response.content)

        # Écrire les détails du livre dans le CSV
        writter.writerow([url, upc, title, price_exact_tax, price_incl_tax, availability, description, category, review_rating, image_url])

# Exemple d'appel de la fonction
# scrap_page_book("https://books.toscrape.com/catalogue/libertarianism-for-beginners_982/index.html", "book")