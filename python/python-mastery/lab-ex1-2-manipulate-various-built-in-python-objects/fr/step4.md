# Partie 4 : Dictionnaires

Dans les dernières parties, vous avez simplement travaillé avec des symboles boursiers. Cependant, supposons que vous vouliez associer des symboles boursiers à d'autres données telles que le prix? Utilisez un dictionnaire :

```python
>>> prices = { 'IBM': 91.1, 'GOOG': 490.1, 'AAPL':312.23 }
>>>
```

Un dictionnaire associe des clés à des valeurs. Voici comment y accéder :

```python
>>> prices['IBM']
91.1
>>> prices['IBM'] = 123.45
>>> prices['HPQ'] = 26.15
>>> prices
{'GOOG': 490.1, 'AAPL': 312.23, 'IBM': 123.45, 'HPQ': 26.15}
>>>
```

Pour obtenir une liste des clés, utilisez ceci :

```python
>>> list(prices)
['GOOG', 'AAPL', 'IBM', 'HPQ']
>>>
```

Pour supprimer une valeur, utilisez `del`

```python
>>> del prices['AAPL']
>>> prices
{'GOOG': 490.1, 'IBM': 123.45, 'HPQ': 26.15}
>>>
```
