# Exécuter une fonction pour chaque élément de liste à l'envers

Écrivez une fonction `for_each_right(itr, fn)` qui prend une liste `itr` et une fonction `fn` en arguments. La fonction devrait exécuter `fn` une fois pour chaque élément de `itr`, en commençant par le dernier.

```python
def for_each_right(itr, fn):
  for el in itr[::-1]:
    fn(el)
```

```python
for_each_right([1, 2, 3], print) # 3 2 1
```
