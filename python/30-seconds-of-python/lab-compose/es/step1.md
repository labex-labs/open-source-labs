# Componer funciones

Escribe una función llamada `compose(*fns)` que acepte una o más funciones como argumentos y devuelva una nueva función que es el resultado de la composición de las funciones de entrada de derecha a izquierda. La última (más a la derecha) función puede aceptar uno o más argumentos; el resto de las funciones deben ser unarias.

```python
from functools import reduce

def compose(*fns):
  return reduce(lambda f, g: lambda *args: f(g(*args)), fns)
```

```python
add5 = lambda x: x + 5
multiply = lambda x, y: x * y
multiply_and_add_5 = compose(add5, multiply)
multiply_and_add_5(5, 2) # 15
```
