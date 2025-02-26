# Cas d'utilisation

Les compréhensions de liste sont d'une utilité immense. Par exemple, vous pouvez collecter les valeurs d'un champ spécifique d'un dictionnaire :

```python
stocknames = [s['name'] for s in stocks]
```

Vous pouvez effectuer des requêtes similaires à celles d'une base de données sur des séquences.

```python
a = [s for s in stocks if s['price'] > 100 and s['shares'] > 50 ]
```

Vous pouvez également combiner une compréhension de liste avec une réduction de séquence :

```python
cost = sum([s['shares']*s['price'] for s in stocks])
```
