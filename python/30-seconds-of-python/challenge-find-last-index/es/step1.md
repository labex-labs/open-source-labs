# Encuentra el último índice coincidente

## Problema

Escribe una función `find_last_index(lst, fn)` que tome una lista `lst` y una función `fn` como argumentos. La función debe devolver el índice del último elemento en `lst` para el cual `fn` devuelve `True`. Si ningún elemento satisface la condición, la función debe devolver `-1`.

## Ejemplo

```python
find_last_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 2
find_last_index([2, 4, 6, 8], lambda n: n % 2 == 1) # -1
```
