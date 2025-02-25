# Exercice 2.2 : Les dictionnaires comme structure de données

Une alternative au tuple est de créer un dictionnaire à la place.

```python
>>> d = {
        'name' : row[0],
      'shares' : int(row[1]),
        'price'  : float(row[2])
    }
>>> d
{'name': 'AA','shares': 100, 'price': 32.2 }
>>>
```

Calculez le coût total de cette position :

```python
>>> cost = d['shares'] * d['price']
>>> cost
3220.0000000000005
>>>
```

Comparez cet exemple avec le même calcul impliquant des tuples ci-dessus. Changez le nombre d'actions en 75.

```python
>>> d['shares'] = 75
>>> d
{'name': 'AA','shares': 75, 'price': 32.2 }
>>>
```

Contrairement aux tuples, les dictionnaires peuvent être modifiés librement. Ajoutez quelques attributs :

```python
>>> d['date'] = (6, 11, 2007)
>>> d['account'] = 12345
>>> d
{'name': 'AA','shares': 75, 'price':32.2, 'date': (6, 11, 2007), 'account': 12345}
>>>
```
