# Convertir número en lista de dígitos

Escribe una función `digitize(n)` que tome un entero no negativo `n` como entrada y devuelva una lista de sus dígitos. La función debe lograr esto realizando los siguientes pasos:

1. Convierte el número de entrada `n` en una cadena de caracteres (string).
2. Utiliza la función `map()` combinada con la función `int` para convertir cada carácter de la cadena en un entero.
3. Devuelve la lista resultante de enteros.

Por ejemplo, si el número de entrada es `123`, la función debe devolver la lista `[1, 2, 3]`.

```python
def digitize(n):
  return list(map(int, str(n)))
```

```python
digitize(123) # [1, 2, 3]
```
