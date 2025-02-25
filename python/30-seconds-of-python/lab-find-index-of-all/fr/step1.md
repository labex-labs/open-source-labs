# Trouver tous les index correspondants

Écrivez une fonction `trouver_index_de_tous(lst, fn)` qui prend une liste `lst` et une fonction de test `fn` en arguments et renvoie une liste d'index de tous les éléments de `lst` pour lesquels `fn` renvoie `True`.

### Entrée

- Une liste `lst` d'entiers.
- Une fonction de test `fn` qui prend un entier en entrée et renvoie une valeur booléenne.

### Sortie

- Une liste d'entiers représentant les index de tous les éléments de `lst` pour lesquels `fn` renvoie `True`.

```python
def trouver_index_de_tous(lst, fn):
  return [i for i, x in enumerate(lst) if fn(x)]
```

```python
trouver_index_de_tous([1, 2, 3, 4], lambda n: n % 2 == 1) # [0, 2]
```
