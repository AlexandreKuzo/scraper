import os
import csv
import requests
from bs4 import BeautifulSoup

# fichier de récupération des catégories de livres
request = requests.get("http://books.toscrape.com/index.html")
page = request.content
soup = BeautifulSoup(request.text, "html.parser")
categories = soup.find("div", {'class':'side_categories'})
token = "https://books.toscrape.com/"


# fonction de récupération des URL des catégories de livres
def get_books(token, href):
    books = []
    for a in categories.find_all('a', href=True):
        j = (token + a['href'])
        books.append(j)
    return books

books = get_books(token, 51)
del books[0] # on supprime de la liste le premier lien (page index)

#fonction d'ouverture d'un lien depuis la catégorie
for book in books:
    request = requests.get(book, verify=False)
    books_spots = soup.find("ol") 
    books_links = books_spots.find_all("h3")
    token = "http://books.toscrape.com/catalogue/"
    def get_links():
        links = []
        for a in books_spots.find_all('a', href=True):
            a['href'] = a['href'].replace('../../../', '')
            j =  token + a['href']
            links.append(j)
            return links
    links = get_links()

print(links)


