# Exercice 2.26 : Le panorama global

En utilisant les techniques de cet exercice, vous pourriez écrire des instructions qui convertissent facilement les champs à partir de presque tout fichier de données orienté colonnes en un dictionnaire Python.

Pour illustrer, supposons que vous lisez des données à partir d'un autre fichier de données comme ceci :

```python
>>> f = open('dowstocks.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> row = next(rows)
>>> headers
['name', 'price', 'date', 'time', 'change', 'open', 'high', 'low', 'volume']
>>> row
['AA', '39.48', '6/11/2007', '9:36am', '-0.18', '39.67', '39.69', '39.45', '181800']
>>>
```

Convertissons les champs en utilisant un truc similaire :

```python
>>> types = [str, float, str, str, float, float, float, float, int]
>>> converted = [func(val) for func, val in zip(types, row)]
>>> record = dict(zip(headers, converted))
>>> record
{'volume': 181800, 'name': 'AA', 'price': 39.48, 'high': 39.69,
'low': 39.45, 'time': '9:36am', 'date': '6/11/2007', 'open': 39.67,
'change': -0.18}
>>> record['name']
'AA'
>>> record['price']
39.48
>>>
```

Bonus : Comment modifieriez-vous cet exemple pour analyser en outre l'entrée `date` en un tuple tel que `(6, 11, 2007)`?

Prenez le temps de réfléchir à ce que vous avez fait dans cet exercice. Nous reviendrons sur ces idées un peu plus tard.
