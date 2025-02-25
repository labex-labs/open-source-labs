# Fusionner des listes

Écrivez une fonction appelée `merge(*args, fill_value=None)` qui prend deux ou plusieurs listes en arguments et renvoie une liste de listes. La fonction devrait combiner les éléments de chaque liste d'entrée en fonction de leurs positions. Si une liste est plus courte que la liste la plus longue, la fonction devrait utiliser `fill_value` pour les éléments restants. Si `fill_value` n'est pas fourni, il devrait par défaut être `None`.

Votre tâche est d'implémenter la fonction `merge()`.

```python
def merge(*args, fill_value = None):
  max_length = max([len(lst) for lst in args])
  result = []
  for i in range(max_length):
    result.append([
      args[k][i] if i < len(args[k]) else fill_value for k in range(len(args))
    ])
  return result
```

```python
merge(['a', 'b'], [1, 2], [True, False]) # [['a', 1, True], ['b', 2, False]]
merge(['a'], [1, 2], [True, False]) # [['a', 1, True], [None, 2, False]]
merge(['a'], [1, 2], [True, False], fill_value = '_')
# [['a', 1, True], ['_', 2, False]]
```
