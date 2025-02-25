# Componer funciones en orden inverso

## Problema

Escribe una función `compose_right` que tome una o más funciones como argumentos y devuelva una nueva función que realice la composición de funciones de izquierda a derecha. La primera (más a la izquierda) función puede aceptar uno o más argumentos; el resto de las funciones deben ser unarias.

Tu implementación debe utilizar la función `reduce` del módulo `functools` para realizar la composición de funciones de izquierda a derecha.

```python
from functools import reduce

def compose_right(*fns):
  # tu código aquí
```

## Ejemplo

```python
add = lambda x, y: x + y
square = lambda x: x * x
add_and_square = compose_right(add, square)
assert add_and_square(1, 2) == 9
```

En el ejemplo anterior, definimos dos funciones `add` y `square`. Luego utilizamos la función `compose_right` para crear una nueva función `add_and_square` que primero suma dos números y luego eleva el resultado al cuadrado. Luego llamamos a la función `add_and_square` con los argumentos `1` y `2`, lo que devuelve `9`.
