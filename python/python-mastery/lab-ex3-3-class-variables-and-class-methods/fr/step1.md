# Laboratoire précédent

Les instances de la classe `Stock` définie dans le laboratoire précédent sont normalement créées comme suit :

```python
>>> s = Stock('GOOG', 100, 490.1)
>>>
```

Cependant, la fonction `read_portfolio()` crée également des instances à partir des lignes de données lues à partir de fichiers. Par exemple, on utilise du code tel que le suivant :

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>> s = Stock(row[0], int(row[1]), float(row[2]))
>>>
```
