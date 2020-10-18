import os
import csv
import requests
from bs4 import BeautifulSoup

#écriture des headers en fichier
headers = ['UPC','Product Type','Price (excl. tax)','Price (incl. tax)','Tax','Availability','Number of reviews','product_page_url','category' ]
with open('individual.csv', 'a', encoding="utf-8") as file:
        writer = csv.writer(file) 
        writer = writer.writerow(headers)


#importation des url pour chaque livre du site
from getcattests import links  # on importe les livres présents sur chaque page de catégorie
from listurls import extra_links # on importe les livres qui doivent être récupérés après avoir géré la pagination dans certaines catégories
urls = links + extra_links # on fusionne les deux listes avant le travail de scraping

#utilisation des bibliothèques request et BeautifulSoup et travail de scrap sur chaque URL ; on itère sur la liste fusionnée
for url in urls:
    request = requests.get(url, verify=False)
    page = request.content
    soup = BeautifulSoup(request.text, "html.parser")

    # Stockage de l'url dans une variable
    product_page_url = request.url

    # Récupération de la catégorie
    links = soup.find_all("a", href=True)
    links = [elt.text for elt in links]
    links[0:3] = []
    links[1:13] = []

    # Récupération de l'url d'image
    image = soup.find("div", {'class' : 'item active'})
    photo = soup.find('img').attrs['src']

    #Récupération des éléments de tableau récap pour le livre
    table = soup.find("table") # Tout le tableau
    items = table.find_all("th") # Les différents paragraphes
    items_list = [elt.text for elt in items] # Déclaration de la liste
    items_list.append('product_page_url') # Ajout de l'Url en fin de liste
    items_list.append('category') # Ajout des liens en fin de liste


    # Récupération du contenu des éléments de tableau avant l'écriture en fichier
    values = soup.find_all("td")
    values_list = [elt.text for elt in values]
    values_list.append(product_page_url)
    values_list.append(links)


    # Ecriture des listes en fichier

    with open('individual.csv', 'a', encoding="utf-8") as file:
        writer = csv.writer(file) 
        writer.writerow(values_list)
        
    

