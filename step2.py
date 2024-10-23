from bs4 import BeautifulSoup
import requests, csv
from step1 import scrap_page_book

def scrap_category(url, csv_name):
    """
    Scrape les livres d'une catégorie donnée depuis l'URL et les écrit dans un fichier CSV.

    Args:
        url (str): L'URL de la catégorie à scraper.
        csv_name (str): Le nom du fichier CSV dans lequel écrire les détails des livres.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    all_a = []

    try:
        li = soup.find('li', class_='current').text
        li_clean = li.replace(' ', '').replace('\n', '')
        number_page = int(li_clean[-1])
        url = url.replace('index.html', 'page-')

        for i in range(1, number_page + 1):
            url_category = f"{url}{i}.html"
            response = requests.get(url_category)
            soup = BeautifulSoup(response.text, 'html.parser')

            divs = soup.find_all('div', class_='image_container')
            for div in divs:
                a = div.find('a')['href']
                a_clean = a.replace('../../../', 'https://books.toscrape.com/catalogue/')
                all_a.append(a_clean)

    except Exception as e:
        divs = soup.find_all('div', class_='image_container')
        for div in divs:
            a = div.find('a')['href']
            a_clean = a.replace('../../../', 'https://books.toscrape.com/catalogue/')
            all_a.append(a_clean)

    for j in range(len(all_a)):
        scrap_page_book(all_a[j], csv_name)

# Exemple d'appel de la fonction
# scrap_category("https://books.toscrape.com/catalogue/category/books/mystery_3/index.html", "mystery")