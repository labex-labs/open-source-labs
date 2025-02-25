# Función Curry

Escribe una función `curry(fn, *args)` que realice la currying de una función dada `fn`. La función debe devolver una nueva función que se comporte como `fn` con los argumentos dados, `args`, aplicados parcialmente.

```python
from functools import partial

def curry(fn, *args):
  return partial(fn, *args)
```

```python
add = lambda x, y: x + y
add10 = curry(add, 10)
add10(20) # 30
```
