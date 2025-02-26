# Exercice 2.23 : Extraction de données à partir de fichiers CSV

Savoir utiliser diverses combinaisons de compréhensions de listes, d'ensembles et de dictionnaires peut être utile dans diverses formes de traitement de données. Voici un exemple qui montre comment extraire des colonnes sélectionnées à partir d'un fichier CSV.

Tout d'abord, lisez une ligne d'informations d'en-tête à partir d'un fichier CSV :

```python
>>> import csv
>>> f = open('portfoliodate.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['name', 'date', 'time','shares', 'price']
>>>
```

Ensuite, définissez une variable qui liste les colonnes qui vous intéressent réellement :

```python
>>> select = ['name','shares', 'price']
>>>
```

Maintenant, localisez les indices des colonnes ci-dessus dans le fichier CSV source :

```python
>>> indices = [ headers.index(colname) for colname in select ]
>>> indices
[0, 3, 4]
>>>
```

Enfin, lisez une ligne de données et convertissez-la en un dictionnaire en utilisant une compréhension de dictionnaire :

```python
>>> row = next(rows)
>>> record = { colname: row[index] for colname, index in zip(select, indices) }   # dict-comprehension
>>> record
{'price': '32.20', 'name': 'AA','shares': '100'}
>>>
```

Si vous vous sentez à l'aise avec ce qui vient de se passer, lisez le reste du fichier :

```python
>>> portfolio = [ { colname: row[index] for colname, index in zip(select, indices) } for row in rows ]
>>> portfolio
[{'price': '91.10', 'name': 'IBM','shares': '50'}, {'price': '83.44', 'name': 'CAT','shares': '150'},
  {'price': '51.23', 'name': 'MSFT','shares': '200'}, {'price': '40.37', 'name': 'GE','shares': '95'},
  {'price': '65.10', 'name': 'MSFT','shares': '50'}, {'price': '70.44', 'name': 'IBM','shares': '100'}]
>>>
```

Oh mon Dieu, vous venez de réduire une grande partie de la fonction `read_portfolio()` à une seule instruction.
