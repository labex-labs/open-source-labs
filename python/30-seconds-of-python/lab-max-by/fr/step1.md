# Trouver la valeur maximale d'une liste en fonction d'une fonction

Écrivez une fonction `max_by(lst, fn)` qui prend une liste `lst` et une fonction `fn` en arguments. La fonction devrait mapper chaque élément de `lst` à une valeur en utilisant la fonction `fn` fournie, puis renvoyer la valeur maximale.

```python
def max_by(lst, fn):
  return max(map(fn, lst))
```

```python
max_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 8
```
