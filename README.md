# Du WebScraping avec Python

Un programme pour récupérer les informations du site web (test) https://books.toscrape.com/index.html ; les données sont ensuite entrées dans un .csv pour traitement et faire ce qu'on veut dans un Excel.

## Contenu du dossier

Le dossier scraper contient 5 fichiers .py qui travaillent ensemble. C'est à partir du fichier "indiviscraper" qu'on fait le travail final (extraction des données et écriture en CSV).
Les 4 autres fichiers permettent de récupérer des catégories de livres et les URL respectives.

### "Matos" requis

- Python 3
- L'installateur de modules Pip et Virtualenv ; infos : https://docs.python.org/fr/3/installing/index.html
- BeautifulSoup : https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Module requests : https://www.w3schools.com/python/module_requests.asp

### Installation et démarrage (consignes adaptées pour utilisateurs/utilisatrices de Mac)

Etape 1: depuis le terminal créer un dossier avec la commande ``mkdir nom_du_dossier``

Etape 2: naviguez dans le dossier tout juste avec la commande ``cd nom_du_dossier``et ensuite crééz un dossier pour l'environnement virtuel (virtualenv) avec la commande ``mkdir nom_du_nouveaudossier``

Etape 3: récupérez les 5 fichiers .py du repo et placez-les dans le dossier princpal "nom_du_dossier".

Etape 4: installez virtualenv pour créer votre environnement virtuel et faire fonctionner votre programme.
Commande ``pip install virtualenv`` ; une fois l'installation faite les dossiers bin, include, lib et le fichier pyvenv.cfg doivent apparaître.

Etape 5: dans le terminal, revenez au dossier principal en tapant les commandes ``cd``(retour à la base) puis ``cd nom_du_dossier``
Activez ensuite l'environnement virtuel avec la commande ``source bin/activate``
Le programme est prêt à travailler en Python. Les commandes pour le faire fonctionner commenceront avec ``python3 nom_du_fichier.py``

## Executer le script

Tout se joue dans le fichier "indiviscraper.py" ; pour l'exécuter il vous suffira de taper la commande ``python3 indiviscraper.py`` ; veillez à bien avoir les 4 autres fichiers dans le même dossier car ils travaillent tous ensemble pour scraper les données !



## Auteur
* **Alexandre Kuzo**  [@alexandrekuzo](https://github.com/AlexandreKuzo)


