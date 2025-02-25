# Liste de sommes partielles

## Problème

Écrivez une fonction `partial_sum(lst)` qui prend une liste de nombres en argument et renvoie une liste de sommes partielles. Votre fonction doit effectuer les étapes suivantes :

1. Utilisez `itertools.accumulate()` pour créer la somme accumulée pour chaque élément de la liste.
2. Utilisez `list()` pour convertir le résultat en une liste.
3. Retournez la liste des sommes partielles.

## Exemple

```python
partial_sum([1, 2, 3, 4, 5]) # [1, 3, 6, 10, 15]
partial_sum([2, 4, 6, 8, 10]) # [2, 6, 12, 20, 30]
partial_sum([5, 10, 15, 20, 25]) # [5, 15, 30, 50, 75]
```
