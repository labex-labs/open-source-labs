# Formatage de dictionnaires

Vous pouvez utiliser la méthode `format_map()` pour appliquer le formatage de chaînes de caractères à un dictionnaire de valeurs :

```python
>>> s = {
    'nom': 'IBM',
    'actions': 100,
    'prix': 91.1
}
>>> '{nom:>10s} {actions:10d} {prix:10.2f}'.format_map(s)
'       IBM        100      91,10'
>>>
```

Elle utilise les mêmes codes que les `f-strings` mais prend les valeurs dans le dictionnaire fourni.
