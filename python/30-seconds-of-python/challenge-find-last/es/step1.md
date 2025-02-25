# Encuentra el último valor coincidente

## Problema

Escribe una función `find_last(lst, fn)` que tome una lista `lst` y una función de prueba `fn` como argumentos. La función debe devolver el valor del último elemento en `lst` para el cual `fn` devuelva `True`. Si ningún elemento satisface la función de prueba, la función debe devolver `None`.

Para resolver este problema, debes usar una comprensión de listas y `next()` para iterar a través de la lista en orden inverso y devolver el último elemento que satisface la función de prueba.

## Ejemplo

```python
find_last([1, 2, 3, 4], lambda n: n % 2 == 1) # 3
find_last([2, 4, 6, 8], lambda n: n % 2 == 1) # None
```

En el primer ejemplo, la función debe devolver `3` porque es el último número impar de la lista. En el segundo ejemplo, la función debe devolver `None` porque no hay números impares en la lista.
