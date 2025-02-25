# Vérifier les doublons dans une fonction de liste

Écrivez une fonction Python appelée `has_duplicates(lst)` qui prend une liste en argument et renvoie `True` si la liste contient des éléments dupliqués, sinon renvoie `False`.

Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Convertissez la liste en un ensemble pour supprimer les doublons.
2. Comparez la longueur de l'ensemble avec la longueur de la liste d'origine.
3. Si les longueurs sont égales, alors la liste n'a pas de doublons, sinon elle en a.

```python
def all_unique(lst):
  return len(lst) == len(set(lst))
```

```python
x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 2, 3, 4, 5]
all_unique(x) # True
all_unique(y) # False
```
