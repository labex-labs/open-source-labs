# Trouver la valeur minimale d'une liste en fonction d'une fonction

Écrivez une fonction appelée `min_by(lst, fn)` qui prend une liste `lst` et une fonction `fn` en arguments. La fonction devrait mapper chaque élément de la liste à une valeur en utilisant la fonction fournie, puis retourner la valeur minimale.

```python
def min_by(lst, fn):
  return min(map(fn, lst))
```

```python
min_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 2
```
