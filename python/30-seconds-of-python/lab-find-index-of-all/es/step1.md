# Encuentra todos los índices coincidentes

Escribe una función `find_index_of_all(lst, fn)` que tome una lista `lst` y una función de prueba `fn` como argumentos y devuelva una lista de índices de todos los elementos en `lst` para los cuales `fn` devuelve `True`.

### Entrada

- Una lista `lst` de enteros.
- Una función de prueba `fn` que tome un entero como entrada y devuelva un valor booleano.

### Salida

- Una lista de enteros que representan los índices de todos los elementos en `lst` para los cuales `fn` devuelve `True`.

```python
def find_index_of_all(lst, fn):
  return [i for i, x in enumerate(lst) if fn(x)]
```

```python
find_index_of_all([1, 2, 3, 4], lambda n: n % 2 == 1) # [0, 2]
```
