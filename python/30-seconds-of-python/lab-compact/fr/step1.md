# Compact List

Écrivez une fonction `compact(lst)` qui prend une liste en argument et renvoie une nouvelle liste avec toutes les valeurs fausses supprimées. Les valeurs fausses incluent `False`, `None`, `0` et `""`.

Pour résoudre ce problème, vous pouvez utiliser la fonction `filter()` pour filtrer les valeurs fausses de la liste.

```python
def compact(lst):
  return list(filter(None, lst))
```

```python
compact([0, 1, False, 2, '', 3, 'a', 's', 34]) # [ 1, 2, 3, 'a', 's', 34 ]
```
