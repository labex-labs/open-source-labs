# Travailler avec les dictionnaires et les données CSV

Commençons par examiner un simple ensemble de données sur les titres d'actions. Dans cette étape, vous apprendrez à lire des données à partir d'un fichier CSV et à les stocker dans un format structuré en utilisant des dictionnaires.

Un fichier CSV (Comma-Separated Values, valeurs séparées par des virgules) est un moyen courant de stocker des données tabulaires, où chaque ligne représente une ligne et les valeurs sont séparées par des virgules. Les dictionnaires en Python sont une puissante structure de données qui vous permet de stocker des paires clé - valeur. En utilisant des dictionnaires, nous pouvons organiser les données du fichier CSV d'une manière plus significative.

Tout d'abord, créez un nouveau fichier Python dans le WebIDE en suivant ces étapes :

1. Cliquez sur le bouton "New File" dans le WebIDE.
2. Nommez le fichier `readport.py`.
3. Copiez et collez le code suivant dans le fichier :

```python
# readport.py

import csv

# A function that reads a file into a list of dictionaries
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)   # Skip the header row
        for row in rows:
            record = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(record)
    return portfolio
```

Ce code définit une fonction `read_portfolio` qui effectue plusieurs tâches importantes :

1. Il ouvre un fichier CSV spécifié par le paramètre `filename`. La fonction `open` est utilisée pour accéder au fichier, et l'instruction `with` garantit que le fichier est correctement fermé après avoir terminé de le lire.
2. Il saute la ligne d'en-tête. La ligne d'en-tête contient généralement les noms des colonnes dans le fichier CSV. Nous utilisons `next(rows)` pour déplacer l'itérateur à la ligne suivante, sautant ainsi l'en-tête.
3. Pour chaque ligne de données, il crée un dictionnaire. Les clés du dictionnaire sont 'name', 'shares' et 'price'. Ces clés nous aideront à accéder aux données de manière plus intuitive.
4. Il convertit le nombre d'actions en entiers et les prix en nombres à virgule flottante. Cela est important car les données lues à partir du fichier CSV sont initialement au format chaîne de caractères, et nous avons besoin de valeurs numériques pour les calculs.
5. Il ajoute chaque dictionnaire à une liste appelée `portfolio`. Cette liste contiendra tous les enregistrements du fichier CSV.
6. Enfin, il retourne la liste complète de dictionnaires.

Maintenant, créons un fichier pour les données de transport en commun. Créez un nouveau fichier appelé `readrides.py` avec le contenu suivant :

```python
# readrides.py

import csv

def read_rides_as_dicts(filename):
    """
    Read the CTA bus data as a list of dictionaries
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)   # Skip header
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides
            }
            records.append(record)
    return records
```

La fonction `read_rides_as_dicts` fonctionne de manière similaire à la fonction `read_portfolio`. Elle lit un fichier CSV lié aux données des bus de l'Autorité de transport de Chicago (CTA), saute la ligne d'en-tête, crée un dictionnaire pour chaque ligne de données et stocke ces dictionnaires dans une liste.

Maintenant, testons la fonction `read_portfolio` en ouvrant un terminal dans le WebIDE :

1. Cliquez sur le menu "Terminal" et sélectionnez "New Terminal".
2. Lancez l'interpréteur Python en tapant `python3`.
3. Exécutez les commandes suivantes :

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> from pprint import pprint
>>> pprint(portfolio)
[{'name': 'AA', 'price': 32.2, 'shares': 100},
 {'name': 'IBM', 'price': 91.1, 'shares': 50},
 {'name': 'CAT', 'price': 83.44, 'shares': 150},
 {'name': 'MSFT', 'price': 51.23, 'shares': 200},
 {'name': 'GE', 'price': 40.37, 'shares': 95},
 {'name': 'MSFT', 'price': 65.1, 'shares': 50},
 {'name': 'IBM', 'price': 70.44, 'shares': 100}]
```

La fonction `pprint` (affichage formaté) est utilisée ici pour afficher les données dans un format plus lisible. Chaque élément de la liste est un dictionnaire représentant une action détenue. Le dictionnaire a les clés suivantes :

- Un symbole d'action (`name`) : C'est l'abréviation utilisée pour identifier l'action.
- Nombre d'actions détenues (`shares`) : Cela indique combien d'actions de l'action sont détenues.
- Prix d'achat par action (`price`) : C'est le prix auquel chaque action a été achetée.

Notez que certaines actions comme 'MSFT' et 'IBM' apparaissent plusieurs fois. Cela représente différents achats de la même action, qui ont peut - être été effectués à différents moments et à différents prix.
