# Intersección de listas basada en función

## Problema

Escribe una función `intersection_by(a, b, fn)` que tome dos listas `a` y `b`, y una función `fn`. La función debe devolver una lista de elementos que existen en ambas listas, después de aplicar la función proporcionada a cada elemento de ambas listas.

### Entrada

- Dos listas `a` y `b` (1 <= len(a), len(b) <= 1000)
- Una función `fn` que tome un argumento y devuelva un valor

### Salida

- Una lista de elementos que existen en ambas listas, después de aplicar la función proporcionada a cada elemento de ambas listas.

## Ejemplo

```python
intersection_by([2.1, 1.2], [2.3, 3.4], floor) # [2.1]
```

### Nota

En el ejemplo anterior, la función `floor()` se aplica a cada elemento de ambas listas. Los conjuntos resultantes son `{2, 3}` y `{2, 1}`. La intersección de estos conjuntos es `{2}`, que luego se devuelve como una lista.
