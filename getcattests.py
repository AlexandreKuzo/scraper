import os
import csv
import requests
from bs4 import BeautifulSoup

# reéupération des URL livres dans chaque catégorie de livres
links = []
from getlinks import books # importation de la liste d'URL de catégories depuis le fichier getlinks

for book in books:
    request = requests.get(book, verify=False) # on itère dans la liste books
    page = request.content
    soup = BeautifulSoup(request.text, "html.parser")
    books_links = soup.find_all("h3") # récupération de la balise où se trouve le lien vers l'URL
    for books_link in books_links: # on itère dans la liste des balises où se trouve lien vers l'URL
        a = books_link.find('a') # on récupère l'attribut a
        a['href'] = a['href'].replace('../../../', '') # on supprime les caractères ../../../ pour faire fonctionner les adresses
        link = a['href'] 
        links.append('http://books.toscrape.com/catalogue/' + link) # on concatène les deux parties pour faire des adresses valides


            
        





