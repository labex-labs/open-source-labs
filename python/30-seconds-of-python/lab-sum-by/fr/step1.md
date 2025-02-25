# Somme d'une liste basée sur une fonction

Écrivez une fonction `sum_by(lst, fn)` qui prend une liste `lst` et une fonction `fn` en arguments. La fonction devrait mapper chaque élément de la liste à une valeur en utilisant la fonction fournie, et renvoyer la somme des valeurs.

```python
def sum_by(lst, fn):
  return sum(map(fn, lst))
```

```python
sum_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 20
```
