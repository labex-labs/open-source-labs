# Progresión Aritmética

Escribe una función `arithmetic_progression(n, lim)` que tome dos enteros positivos `n` y `lim` y devuelva una lista de números en la progresión aritmética que comienza con `n` y va hasta `lim`. La función debe usar `range()` y `list()` con los valores de inicio, paso y fin adecuados para generar la lista.

### Entrada

- Dos enteros positivos `n` y `lim` donde `n` es el número de inicio y `lim` es el límite.

### Salida

- Una lista de números en la progresión aritmética que comienza con `n` y va hasta `lim`.

```python
def arithmetic_progression(n, lim):
  return list(range(n, lim + 1, n))
```

```python
arithmetic_progression(5, 25) # [5, 10, 15, 20, 25]
```
