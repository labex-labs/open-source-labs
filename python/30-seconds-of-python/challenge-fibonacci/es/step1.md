# Desafío de Fibonacci

## Problema

Escribe una función llamada `fibonacci(n)` que tome un entero `n` como parámetro y devuelva una lista que contenga la secuencia de Fibonacci hasta el término n.

Para resolver este problema, puedes seguir estos pasos:

1. Crea una lista vacía llamada `secuencia`.
2. Si `n` es menor o igual a 0, agrega 0 a la lista `secuencia` y devuelve la lista.
3. Agrega 0 y 1 a la lista `secuencia`.
4. Utiliza un bucle `while` para agregar la suma de los últimos dos números de la lista `secuencia` al final de la lista, hasta que la longitud de la lista alcance `n`.
5. Devuelve la lista `secuencia`.

## Ejemplo

```python
fibonacci(7) # [0, 1, 1, 2, 3, 5, 8, 13]
```
