# Roter les éléments d'une liste

Écrivez une fonction `roll(lst, offset)` qui prend une liste `lst` et un entier `offset`. La fonction doit déplacer le nombre spécifié d'éléments au début de la liste. Si `offset` est positif, les éléments doivent être déplacés de la fin de la liste au début. Si `offset` est négatif, les éléments doivent être déplacés du début de la liste à la fin.

Retournez la liste modifiée.

```python
def roll(lst, offset):
  return lst[-offset:] + lst[:-offset]
```

```python
roll([1, 2, 3, 4, 5], 2) # [4, 5, 1, 2, 3]
roll([1, 2, 3, 4, 5], -2) # [3, 4, 5, 1, 2]
```
