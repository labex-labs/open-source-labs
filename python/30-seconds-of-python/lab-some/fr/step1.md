# Vérifiez si certains éléments de la liste sont évalués à True

Écrivez une fonction `some(lst, fn)` qui prend une liste `lst` et une fonction `fn` en arguments. La fonction doit renvoyer `True` si la fonction `fn` renvoie `True` pour au moins un élément de la liste `lst`. Si aucun élément de la liste ne satisfait la condition, la fonction doit renvoyer `False`. Si aucune fonction n'est fournie, la fonction doit utiliser la fonction identité (qui renvoie l'élément lui-même).

```python
def some(lst, fn = lambda x: x):
  return any(map(fn, lst))
```

```python
some([0, 1, 2, 0], lambda x: x >= 2 ) # True
some([0, 0, 1, 0]) # True
```
