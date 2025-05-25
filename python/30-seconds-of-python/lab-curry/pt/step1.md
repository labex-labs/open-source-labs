# Função Curry

Escreva uma função `curry(fn, *args)` que currifique uma função dada `fn`. A função deve retornar uma nova função que se comporta como `fn` com os argumentos dados, `args`, parcialmente aplicados.

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
