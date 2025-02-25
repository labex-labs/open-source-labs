# Rotar elementos de una lista

## Problema

Escribe una función `roll(lst, offset)` que tome una lista `lst` y un entero `offset`. La función debe mover la cantidad especificada de elementos al principio de la lista. Si `offset` es positivo, los elementos deben moverse desde el final de la lista hasta el principio. Si `offset` es negativo, los elementos deben moverse desde el principio de la lista hasta el final.

Devuelve la lista modificada.

## Ejemplo

```python
roll([1, 2, 3, 4, 5], 2) # [4, 5, 1, 2, 3]
roll([1, 2, 3, 4, 5], -2) # [3, 4, 5, 1, 2]
```
