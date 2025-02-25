# Transposer une matrice

## Problème

Écrivez une fonction appelée `transpose(lst)` qui prend une liste bidimensionnelle en argument et renvoie la transposée de la liste donnée.

Suivez ces étapes pour résoudre le problème :

- Utilisez `*lst` pour obtenir la liste fournie sous forme de tuples.
- Utilisez `zip()` en combinaison avec `list()` pour créer la transposée de la liste bidimensionnelle donnée.

## Exemple

```python
transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# [(1, 4, 7, 10), (2, 5, 8, 11), (3, 6, 9, 12)]
```
