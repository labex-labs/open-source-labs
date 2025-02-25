# Queue de liste

Écrivez une fonction `tail(lst)` qui prend une liste en argument et renvoie tous les éléments de la liste sauf le premier. Si la liste ne contient qu'un seul élément, renvoyez la liste entière.

```python
def tail(lst):
  return lst[1:] if len(lst) > 1 else lst
```

```python
tail([1, 2, 3]) # [2, 3]
tail([1]) # [1]
```
