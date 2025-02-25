# Élément le plus fréquent

## Problème

Écrivez une fonction Python appelée `most_frequent(lst)` qui prend une liste d'entiers en entrée et renvoie l'élément le plus fréquent de la liste. Si plusieurs éléments apparaissent avec le même nombre d'occurrences et ont la plus haute fréquence, renvoyez celui qui apparaît en premier dans la liste.

Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Utilisez `set()` pour obtenir les valeurs uniques dans `lst`.
2. Utilisez `max()` pour trouver l'élément qui a le plus d'apparitions.

Votre fonction devrait avoir la signature suivante :

```python
def most_frequent(lst: List[int]) -> int:
```

## Exemple

```python
assert most_frequent([1, 2, 1, 2, 3, 2, 1, 4, 2]) == 2
assert most_frequent([1, 2, 3, 4, 5]) == 1
assert most_frequent([1, 1, 1, 1, 1]) == 1
```
