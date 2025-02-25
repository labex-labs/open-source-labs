# Similitud de listas

## Problema

Escribe una función `similarity(a, b)` que tome dos listas `a` y `b` como argumentos y devuelva una nueva lista que contenga solo los elementos que existen en ambas `a` y `b`.

Para resolver este problema, podemos usar la comprensión de listas para iterar sobre los elementos de `a` y comprobar si existen en `b`. Si un elemento existe en ambas listas, lo agregamos a una nueva lista.

## Ejemplo

```python
similarity([1, 2, 3], [1, 2, 4]) # [1, 2]
```

En este ejemplo, la función `similarity` toma dos listas `[1, 2, 3]` y `[1, 2, 4]` como argumentos. La función devuelve una nueva lista `[1, 2]` que contiene solo los elementos que existen en ambas listas.
