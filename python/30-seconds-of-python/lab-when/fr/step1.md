# Appliquer une fonction lorsque c'est vrai

Écrivez une fonction appelée `when` qui prend deux arguments : une fonction prédicat `predicate` et une fonction à appliquer `when_true`. La fonction `when` devrait renvoyer une nouvelle fonction qui prend un seul argument `x`. La nouvelle fonction devrait vérifier si la valeur de `predicate(x)` est `True`. Si c'est le cas, la nouvelle fonction devrait appeler `when_true(x)` et renvoyer le résultat. Sinon, la nouvelle fonction devrait renvoyer `x`.

```python
def when(predicate, when_true):
  return lambda x: when_true(x) if predicate(x) else x
```

```python
double_even_numbers = when(lambda x: x % 2 == 0, lambda x : x * 2)
double_even_numbers(2) # 4
double_even_numbers(1) # 1
```
