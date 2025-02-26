# Propriétés pour les attributs calculés

Plus tôt, vous avez défini une classe `Stock`. Par exemple :

```python
>>> s = Stock('GOOG',100,490.10)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
>>> s.cost()
49010.0
>>>
```

En utilisant une propriété, convertissez `cost()` en un attribut qui n'a plus besoin des parenthèses. Par exemple :

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.cost               # Propriété. Calcule le coût
49010.0
>>>
```
