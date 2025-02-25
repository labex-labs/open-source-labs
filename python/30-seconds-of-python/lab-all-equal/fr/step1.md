# Vérifiez si les éléments d'une liste sont identiques

Écrivez une fonction `all_equal(lst)` qui prend une liste en argument et renvoie `True` si tous les éléments de la liste sont identiques, et `False` sinon.

Pour résoudre ce problème, vous pouvez suivre les étapes suivantes :

1. Utilisez `set()` pour éliminer les éléments dupliqués de la liste.
2. Utilisez `len()` pour vérifier si la longueur de l'ensemble est `1`.
3. Si la longueur de l'ensemble est `1`, renvoyez `True`. Sinon, renvoyez `False`.

```python
def all_equal(lst):
  return len(set(lst)) == 1
```

```python
all_equal([1, 2, 3, 4, 5, 6]) # False
all_equal([1, 1, 1, 1]) # True
```
