# Exercice 2.21 : Requêtes sur des données

Essayez les exemples suivants de diverses requêtes sur des données.

Tout d'abord, une liste de toutes les positions du portefeuille avec plus de 100 actions.

```python
>>> more100 = [ s for s in portfolio if s['shares'] > 100 ]
>>> more100
[{'price': 83.44, 'name': 'CAT','shares': 150}, {'price': 51.23, 'name': 'MSFT','shares': 200}]
>>>
```

Toutes les positions du portefeuille pour les actions MSFT et IBM.

```python
>>> msftibm = [ s for s in portfolio if s['name'] in {'MSFT','IBM'} ]
>>> msftibm
[{'price': 91.1, 'name': 'IBM','shares': 50}, {'price': 51.23, 'name': 'MSFT','shares': 200},
  {'price': 65.1, 'name': 'MSFT','shares': 50}, {'price': 70.44, 'name': 'IBM','shares': 100}]
>>>
```

Une liste de toutes les positions du portefeuille qui coûtent plus de 10 000 $.

```python
>>> cost10k = [ s for s in portfolio if s['shares'] * s['price'] > 10000 ]
>>> cost10k
[{'price': 83.44, 'name': 'CAT','shares': 150}, {'price': 51.23, 'name': 'MSFT','shares': 200}]
>>>
```
