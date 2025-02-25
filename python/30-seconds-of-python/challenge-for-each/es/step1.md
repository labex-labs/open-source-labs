# Ejecutar una función para cada elemento de una lista

## Problema

Escribe una función `for_each(itr, fn)` que tome una lista `itr` y una función `fn` como argumentos. La función debe ejecutar `fn` una vez para cada elemento en `itr`.

## Ejemplo

```python
def print_square(num):
    print(num*num)

for_each([1, 2, 3], print_square) # imprime 1 4 9
```

En el ejemplo anterior, la función `for_each` se llama con una lista `[1, 2, 3]` y una función `print_square`. La función `print_square` se ejecuta una vez para cada elemento de la lista, imprimiendo el cuadrado de cada número.
