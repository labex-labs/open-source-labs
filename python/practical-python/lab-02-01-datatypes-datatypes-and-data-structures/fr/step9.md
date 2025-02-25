# Opérations courantes

Pour obtenir des valeurs à partir d'un dictionnaire, utilisez les noms de clés.

```python
>>> print(s['name'], s['shares'])
GOOG 100
>>> s['price']
490.10
>>>
```

Pour ajouter ou modifier des valeurs, utilisez l'affectation avec les noms de clés.

```python
>>> s['shares'] = 75
>>> s['date'] = '6/6/2007'
>>>
```

Pour supprimer une valeur, utilisez l'instruction `del`.

```python
>>> del s['date']
>>>
```
