# Todos los índices de un valor

Escribe una función de Python llamada `index_of_all(lst, value)` que tome una lista `lst` y un valor `value` como argumentos y devuelva una lista de índices de todas las ocurrencias de `value` en `lst`.

Para resolver este problema, puedes usar `enumerate()` y una comprensión de lista para comprobar cada elemento para ver si es igual a `value` y agregar `i` al resultado.

```python
def index_of_all(lst, value):
  return [i for i, x in enumerate(lst) if x == value]
```

```python
index_of_all([1, 2, 1, 4, 5, 1], 1) # [0, 2, 5]
index_of_all([1, 2, 3, 4], 6) # []
```
