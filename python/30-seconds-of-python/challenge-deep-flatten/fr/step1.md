# Aplatir profondément une liste

## Problème

Écrivez une fonction `deep_flatten(lst)` qui prend une liste `lst` en argument et renvoie une nouvelle liste qui est la version aplatie profondément de `lst`. La fonction devrait utiliser la récursion et la fonction `isinstance()` avec `collections.abc.Iterable` pour vérifier si un élément est itérable. Si un élément est itérable, la fonction devrait appliquer `deep_flatten()` de manière récursive à cet élément. Sinon, la fonction devrait renvoyer une liste ne contenant que cet élément.

## Exemple

```python
deep_flatten([1, [2], [[3], 4], 5]) # [1, 2, 3, 4, 5]
deep_flatten([1, [2, [3, [4]]]]) # [1, 2, 3, 4]
deep_flatten([1, 2, 3, 4]) # [1, 2, 3, 4]
deep_flatten([]) # []
```
