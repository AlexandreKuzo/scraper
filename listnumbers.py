import os
import csv
import requests
from bs4 import BeautifulSoup

# fichier gérant la pagination pour les catégories de livres réparties sur plusieurs pages (+ de 20 livres)

from getlinks import books #importation de la liste books (catégories de livres)

list_numbers = [] # on créé une liste
for book in books:
    request = requests.get(book, verify=False)
    page = request.content
    soup = BeautifulSoup(page, "html.parser")
    page_number = soup.find("form")
    number = page_number.find("strong") # on récupère le nombre de livres dans la catégorie
    number = number.text
    number = int(number) # on transforme la variable en chiffres pour la fonction de comparaison
    list_numbers.append(number) # on ajoute la valeur à la liste à chaque tour de boucle

extra_pages = [] # on créé une nouvelle liste
book_list_numbers = zip(books, list_numbers) # on mixe les deux listes (url de catégorie, nombre de livres dans la catégorie)

for a,b in zip(books, list_numbers): # boucle permettant d'itérer sur les deux valeurs, gérées par a et b
    if b > 20 and b < 40: # si on a plus de 20 livres, on ajoute une page 2...
        j = a.replace('/index.html', '') + "/page-2.html"
        extra_pages.append(j)
    elif b > 40 and b < 60: # si on a plus de 40 livres, on ajoute une page 3, etc.
        j = a.replace('/index.html', '') + "/page-2.html"
        k = a.replace('/index.html', '') + "/page-3.html"
        extra_pages.append(j)
        extra_pages.append(k)
    elif b > 60 and b < 80:
        j = a.replace('/index.html', '') + "/page-2.html"
        k = a.replace('/index.html', '') + "/page-3.html"
        l = a.replace('/index.html', '') + "/page-4.html"
        extra_pages.append(j)
        extra_pages.append(k)
        extra_pages.append(l)
    elif b > 80 and b < 100:
        j = a.replace('/index.html', '') + "/page-2.html"
        k = a.replace('/index.html', '') + "/page-3.html"
        l = a.replace('/index.html', '') + "/page-4.html"
        m = a.replace('/index.html', '') + "/page-5.html"
        extra_pages.append(j)
        extra_pages.append(k)
        extra_pages.append(l)
        extra_pages.append(m)
    elif b > 100 and b < 120:
        j = a.replace('/index.html', '') + "/page-2.html"
        k = a.replace('/index.html', '') + "/page-3.html"
        l = a.replace('/index.html', '') + "/page-4.html"
        m = a.replace('/index.html', '') + "/page-5.html"
        n = a.replace('/index.html', '') + "/page-6.html"
        extra_pages.append(j)
        extra_pages.append(k)
        extra_pages.append(l)
        extra_pages.append(m)
        extra_pages.append(n)
    elif b > 120 and b < 140:
        j = a.replace('/index.html', '') + "/page-2.html"
        k = a.replace('/index.html', '') + "/page-3.html"
        l = a.replace('/index.html', '') + "/page-4.html"
        m = a.replace('/index.html', '') + "/page-5.html"
        n = a.replace('/index.html', '') + "/page-6.html"
        o = a.replace('/index.html', '') + "/page-7.html"
        extra_pages.append(j)
        extra_pages.append(k)
        extra_pages.append(l)
        extra_pages.append(m)
        extra_pages.append(n)
        extra_pages.append(o)
    elif b > 140 and b < 160:
        j = a.replace('/index.html', '') + "/page-2.html"
        k = a.replace('/index.html', '') + "/page-3.html"
        l = a.replace('/index.html', '') + "/page-4.html"
        m = a.replace('/index.html', '') + "/page-5.html"
        n = a.replace('/index.html', '') + "/page-6.html"
        o = a.replace('/index.html', '') + "/page-7.html"
        p = a.replace('/index.html', '') + "/page-8.html"
        extra_pages.append(j)
        extra_pages.append(k)
        extra_pages.append(l)
        extra_pages.append(m)
        extra_pages.append(n)
        extra_pages.append(o)
        extra_pages.append(p)
    else:
        pass # si la catégorie a moins de 20, on ne fait rien et on passe à l'URL de catégorie suivante






