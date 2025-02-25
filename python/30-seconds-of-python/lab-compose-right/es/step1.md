# Composición de funciones inversa

Escribe una función `compose_right` que tome una o más funciones como argumentos y devuelva una nueva función que realice la composición de funciones de izquierda a derecha. La primera (más a la izquierda) función puede aceptar uno o más argumentos; las funciones restantes deben ser unarias.

Tu implementación debe utilizar la función `reduce` del módulo `functools` para realizar la composición de funciones de izquierda a derecha.

```python
from functools import reduce

def compose_right(*fns):
  # tu código aquí
```

```python
from functools import reduce

def compose_right(*fns):
  return reduce(lambda f, g: lambda *args: g(f(*args)), fns)
```

```python
add = lambda x, y: x + y
square = lambda x: x * x
add_and_square = compose_right(add, square)
add_and_square(1, 2) # 9
```
