# Chaque nème élément dans une liste

Écrivez une fonction `every_nth(lst, nth)` qui prend une liste `lst` et un entier `nth` en arguments et renvoie une nouvelle liste contenant chaque `nème` élément de la liste d'origine.

```python
def every_nth(lst, nth):
  return lst[nth - 1::nth]
```

```python
every_nth([1, 2, 3, 4, 5, 6], 2) # [ 2, 4, 6 ]
```
