# Exercice 3.3 : Lecture de fichiers CSV

Pour commencer, concentrons-nous seulement sur le problème de la lecture d'un fichier CSV dans une liste de dictionnaires. Dans le fichier `fileparse_3.3.py`, définissez une fonction qui ressemble à ceci :

```python
# fileparse_3.3.py
import csv

def parse_csv(filename):
    '''
    Analyse un fichier CSV en une liste d'enregistrements
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Lit les en-têtes du fichier
        headers = next(rows)
        records = []
        for row in rows:
            if not row:    # Ignore les lignes sans données
                continue
            record = dict(zip(headers, row))
            records.append(record)

    return records
```

Cette fonction lit un fichier CSV dans une liste de dictionnaires tout en cachant les détails de l'ouverture du fichier, de son enveloppement avec le module `csv`, de l'ignorance des lignes vides, etc.

Essayez-le :

Indice : `python3 -i fileparse_3.3.py`.

```python
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv')
>>> portfolio
[{'name': 'AA','shares': '100', 'price': '32.20'}, {'name': 'IBM','shares': '50', 'price': '91.10'}, {'name': 'CAT','shares': '150', 'price': '83.44'}, {'name': 'MSFT','shares': '200', 'price': '51.23'}, {'name': 'GE','shares': '95', 'price': '40.37'}, {'name': 'MSFT','shares': '50', 'price': '65.10'}, {'name': 'IBM','shares': '100', 'price': '70.44'}]
>>>
```

Cela est bon, sauf que vous ne pouvez pas faire de calcul utile avec les données car tout est représenté comme une chaîne de caractères. Nous allons corriger cela bientôt, mais continuons à construire dessus.
