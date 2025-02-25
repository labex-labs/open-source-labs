# Encuentra el índice coincidente

## Problema

Escribe una función `find_index(lst, fn)` que tome una lista `lst` y una función de prueba `fn` como argumentos. La función debe devolver el índice del primer elemento en `lst` para el cual `fn` devuelva `True`.

## Ejemplo

```python
find_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 0
```
