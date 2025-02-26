# Défi

Qu'arrive-t-il lorsqu'on prend une tranche de données de trajet?

```python
>>> r = rows[0:10]
>>> r
... regardez le résultat...
>>>
```

Il va probablement sembler un peu fou. Êtes-vous capable de modifier la classe `RideData` de manière à ce qu'elle produise une tranche correcte qui ressemble à une liste de dictionnaires? Par exemple, comme ceci :

```python
>>> rows = readrides.read_rides_as_columns('ctabus.csv')
>>> rows
<readrides.RideData object at 0x10f5054a8>
>>> len(rows)
577563
>>> r = rows[0:10]
>>> r
<readrides.RideData object at 0x10f5068c8>
>>> len(r)
10
>>> r[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> r[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>>
```
