# Différence de listes

Écrivez une fonction Python appelée `list_difference(a, b)` qui prend deux listes en arguments et renvoie la différence entre elles. La fonction ne doit pas filtrer les valeurs dupliquées. Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Créez un ensemble à partir de la seconde liste `b`.
2. Utilisez une compréhension de liste sur la première liste `a` pour ne conserver que les valeurs qui ne sont pas contenues dans l'ensemble précédemment créé `_b`.
3. Retournez la liste résultante.

```python
def difference(a, b):
  _b = set(b)
  return [item for item in a if item not in _b]
```

```python
difference([1, 2, 3], [1, 2, 4]) # [3]
```
