from bs4 import BeautifulSoup
import requests, csv
from step2 import scrap_category

def scrap_website(url):
    """
    Fonction principale pour scraper les catégories et leurs liens respectifs depuis le site Books to Scrape.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    ul = soup.find('ul', class_='nav nav-list')
    li = ul.find('li')
    a_tags = li.find_all('a')

    # Extraire les catégories et les liens
    categories = [a.text.strip() for a in a_tags]
    links = [a['href'] for a in a_tags]

    # Itérer sur chaque catégorie et lien
    for i in range(0, len(links)):
        scrap_category(f'https://books.toscrape.com/{links[i]}', categories[i])

scrap_website("https://books.toscrape.com/index.html")