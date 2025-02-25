# Similitud de listas

Escribe una función `similarity(a, b)` que tome dos listas `a` y `b` como argumentos y devuelva una nueva lista que contenga solo los elementos que existen en ambas `a` y `b`.

Para resolver este problema, podemos usar la comprensión de listas para iterar sobre los elementos de `a` y comprobar si existen en `b`. Si un elemento existe en ambas listas, lo agregamos a una nueva lista.

```python
def similarity(a, b):
  return [item for item in a if item in b]
```

```python
similarity([1, 2, 3], [1, 2, 4]) # [1, 2]
```
