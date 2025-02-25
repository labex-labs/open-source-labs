# Convertir un número en una lista de dígitos

## Problema

Escribe una función `digitize(n)` que tome un número entero no negativo `n` como entrada y devuelva una lista de sus dígitos. La función debe lograr esto realizando los siguientes pasos:

1. Convertir el número de entrada `n` en una cadena.
2. Utilizar la función `map()` combinada con la función `int` para convertir cada carácter de la cadena en un entero.
3. Devolver la lista resultante de enteros.

Por ejemplo, si el número de entrada es `123`, la función debe devolver la lista `[1, 2, 3]`.

## Ejemplo

```python
assert digitize(123) == [1, 2, 3]
assert digitize(4567) == [4, 5, 6, 7]
assert digitize(0) == [0]
```
