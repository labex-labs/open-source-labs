# Cast to List

Écrivez une fonction `cast_list(val)` qui prend une valeur en argument et la renvoie sous forme de liste. Si la valeur est déjà une liste, renvoyez-la telle quelle. Si la valeur n'est pas une liste mais est itérable, renvoyez-la sous forme de liste. Si la valeur n'est pas itérable, renvoyez-la sous forme d'une liste à un seul élément.

```python
def cast_list(val):
  return list(val) if isinstance(val, (tuple, list, set, dict)) else [val]
```

```python
cast_list('foo') # ['foo']
cast_list([1]) # [1]
cast_list(('foo', 'bar')) # ['foo', 'bar']
```
