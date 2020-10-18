import os
import csv
import requests
from bs4 import BeautifulSoup

extra_links = []
from listnumbers import extra_pages # on importe la liste des URL de catégories "paginées"

for extra_page in extra_pages: # on scrape et fusionne de la même manière que dans le fichier getcattests.py
    request = requests.get(extra_page, verify=False)
    page = request.content
    soup = BeautifulSoup(request.text, "html.parser")
    books_links = soup.find_all("h3")
    for books_link in books_links:
        a = books_link.find('a')
        a['href'] = a['href'].replace('../../../', '')
        link = a['href']
        extra_links.append('http://books.toscrape.com/catalogue/' + link)


