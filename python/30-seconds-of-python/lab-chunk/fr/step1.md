# Diviser une liste en morceaux

Écrivez une fonction `chunk(lst, size)` qui prend une liste `lst` et un entier positif `size` en arguments et renvoie une liste de listes plus petites, dont chacune a une taille maximale de `size`. Si la longueur de `lst` n'est pas divisible uniformément par `size`, la dernière liste de la liste renvoyée devrait contenir les éléments restants.

```python
from math import ceil

def chunk(lst, size):
  return list(
    map(lambda x: lst[x * size:x * size + size],
      list(range(ceil(len(lst) / size)))))
```

```python
chunk([1, 2, 3, 4, 5], 2) # [[1, 2], [3, 4], [5]]
```
