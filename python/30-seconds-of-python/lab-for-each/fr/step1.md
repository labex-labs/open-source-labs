# Exécuter une fonction pour chaque élément de la liste

Écrivez une fonction `for_each(itr, fn)` qui prend une liste `itr` et une fonction `fn` en arguments. La fonction devrait exécuter `fn` une fois pour chaque élément de `itr`.

```python
def for_each(itr, fn):
  for el in itr:
    fn(el)
```

```python
for_each([1, 2, 3], print) # 1 2 3
```
