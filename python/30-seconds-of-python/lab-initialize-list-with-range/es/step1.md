# Inicializar una lista con un rango

Escribe una función `initialize_list_with_range(end, start=0, step=1)` que inicialice una lista que contiene los números en el rango especificado, donde `start` y `end` son inclusivos y su diferencia común es `step`.

La función debe devolver una lista de la longitud adecuada, llena con los valores deseados en el rango dado.

### Entrada

- `end` (entero) - El final del rango (inclusivo).
- `start` (entero, opcional) - El inicio del rango (inclusivo). El valor predeterminado es 0.
- `step` (entero, opcional) - La diferencia común entre cada número en el rango. El valor predeterminado es 1.

### Salida

- Una lista que contiene los números en el rango especificado.

```python
def initialize_list_with_range(end, start = 0, step = 1):
  return list(range(start, end + 1, step))
```

```python
initialize_list_with_range(5) # [0, 1, 2, 3, 4, 5]
initialize_list_with_range(7, 3) # [3, 4, 5, 6, 7]
initialize_list_with_range(9, 0, 2) # [0, 2, 4, 6, 8]
```
