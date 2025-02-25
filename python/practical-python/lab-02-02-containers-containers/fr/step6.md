# Recherches dans les dictionnaires

Vous pouvez tester l'existence d'une clé.

```python
if key in d:
    # OUI
else:
    # NON
```

Vous pouvez rechercher une valeur qui peut ne pas exister et fournir une valeur par défaut au cas où elle n'existerait pas.

```python
name = d.get(key, default)
```

Un exemple :

```python
>>> prices.get('IBM', 0.0)
93.37
>>> prices.get('SCOX', 0.0)
0.0
>>>
```
