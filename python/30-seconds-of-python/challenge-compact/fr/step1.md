# Compact List

## Problème

Écrivez une fonction `compact(lst)` qui prend une liste en argument et renvoie une nouvelle liste sans toutes les valeurs fausses. Les valeurs fausses incluent `False`, `None`, `0` et `""`.

Pour résoudre ce problème, vous pouvez utiliser la fonction `filter()` pour filtrer les valeurs fausses de la liste.

## Exemple

```python
compact([0, 1, False, 2, '', 3, 'a', 's', 34]) # [ 1, 2, 3, 'a', 's', 34 ]
```
