from bs4 import BeautifulSoup
import csv
import os
import requests

def scrap_page_book(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    csv_exist = os.path.isfile('books.csv')

    if not csv_exist:
        with open('books.csv', mode='w', newline='', encoding="utf8") as file:
            writter = csv.writer(file)
            writter.writerow(['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url'])

    with open('books.csv', mode='a', newline='', encoding="utf8") as fichier_csv:
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
        availability = all_td[5]

        ul = soup.find('ul')
        a = ul.find_all('a')
        category = a[-1].text

        review_rating = soup.find('p', class_='star-rating')['class'][1]

        div = soup.find('div', class_='carousel-inner')
        image_url = soup.find('img')['src']

        writter.writerow([url, upc, title, price_exact_tax, price_incl_tax, availability, description, category, review_rating, image_url])

scrap_page_book("https://books.toscrape.com/catalogue/libertarianism-for-beginners_982/index.html")