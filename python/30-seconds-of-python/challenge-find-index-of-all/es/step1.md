# Encuentra todos los índices coincidentes

## Problema

Escribe una función `find_index_of_all(lst, fn)` que tome una lista `lst` y una función de prueba `fn` como argumentos y devuelva una lista de índices de todos los elementos en `lst` para los cuales `fn` devuelve `True`.

### Entrada

- Una lista `lst` de enteros.
- Una función de prueba `fn` que tome un entero como entrada y devuelva un valor booleano.

### Salida

- Una lista de enteros que representan los índices de todos los elementos en `lst` para los cuales `fn` devuelve `True`.

## Ejemplo

```python
find_index_of_all([1, 2, 3, 4], lambda n: n % 2 == 1) # [0, 2]
find_index_of_all([1, 2, 3, 4], lambda n: n > 2) # [2, 3]
find_index_of_all([1, 2, 3, 4], lambda n: n < 0) # []
```

### Nota

- En el primer ejemplo, la función de prueba `lambda n: n % 2 == 1` comprueba si el entero es impar. La función devuelve `[0, 2]` porque los elementos en los índices `0` y `2` de la lista `[1, 2, 3, 4]` son impares.
- En el segundo ejemplo, la función de prueba `lambda n: n > 2` comprueba si el entero es mayor que `2`. La función devuelve `[2, 3]` porque los elementos en los índices `2` y `3` de la lista `[1, 2, 3, 4]` son mayores que `2`.
- En el tercer ejemplo, la función de prueba `lambda n: n < 0` comprueba si el entero es negativo. La función devuelve `[]` porque no hay elementos negativos en la lista `[1, 2, 3, 4]`.
