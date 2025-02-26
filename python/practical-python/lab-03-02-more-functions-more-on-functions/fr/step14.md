# Exercice 3.4 : Construction d'un sélecteur de colonnes

Dans de nombreux cas, vous n'êtes intéressé que par certaines colonnes d'un fichier CSV, pas par toutes les données. Modifiez la fonction `parse_csv()` de sorte qu'elle permette facultativement de sélectionner des colonnes spécifiées par l'utilisateur comme suit :

```python
>>> # Lire toutes les données
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv')
>>> portfolio
[{'name': 'AA','shares': '100', 'price': '32.20'}, {'name': 'IBM','shares': '50', 'price': '91.10'}, {'name': 'CAT','shares': '150', 'price': '83.44'}, {'name': 'MSFT','shares': '200', 'price': '51.23'}, {'name': 'GE','shares': '95', 'price': '40.37'}, {'name': 'MSFT','shares': '50', 'price': '65.10'}, {'name': 'IBM','shares': '100', 'price': '70.44'}]

>>> # Lire seulement certaines données
>>> shares_held = parse_csv('/home/labex/project/portfolio.csv', select=['name','shares'])
>>> shares_held
[{'name': 'AA','shares': '100'}, {'name': 'IBM','shares': '50'}, {'name': 'CAT','shares': '150'}, {'name': 'MSFT','shares': '200'}, {'name': 'GE','shares': '95'}, {'name': 'MSFT','shares': '50'}, {'name': 'IBM','shares': '100'}]
>>>
```

Un exemple de sélecteur de colonnes a été donné dans l'exercice 2.23. Cependant, voici une manière de le faire :

```python
# fileparse_3.4.py
import csv

def parse_csv(filename, select=None):
    '''
    Analyse un fichier CSV en une liste d'enregistrements
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Lit les en-têtes du fichier
        headers = next(rows)

        # Si un sélecteur de colonnes a été donné, trouver les indices des colonnes spécifiées.
        # Rétroalimenter également l'ensemble d'en-têtes utilisés pour les dictionnaires résultants
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:    # Ignore les lignes sans données
                continue
            # Filtrer la ligne si des colonnes spécifiques ont été sélectionnées
            if indices:
                row = [ row[index] for index in indices ]

            # Créer un dictionnaire
            record = dict(zip(headers, row))
            records.append(record)

    return records
```

Il y a un certain nombre de points délicats dans cette partie. Probablement le plus important est la correspondance des sélections de colonnes aux indices de ligne. Par exemple, supposons que le fichier d'entrée ait les en-têtes suivants :

```python
>>> headers = ['name', 'date', 'time','shares', 'price']
>>>
```

Maintenant, supposons que les colonnes sélectionnées soient les suivantes :

```python
>>> select = ['name','shares']
>>>
```

Pour effectuer la sélection appropriée, vous devez mapper les noms de colonnes sélectionnés aux indices de colonne dans le fichier. C'est ce que fait cette étape :

```python
>>> indices = [headers.index(colname) for colname in select ]
>>> indices
[0, 3]
>>>
```

En d'autres termes, "name" est la colonne 0 et "shares" est la colonne 3. Lorsque vous lisez une ligne de données à partir du fichier, les indices sont utilisés pour la filtrer :

```python
>>> row = ['AA', '6/11/2007', '9:50am', '100', '32.20' ]
>>> row = [ row[index] for index in indices ]
>>> row
['AA', '100']
>>>
```
