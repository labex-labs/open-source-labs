# Inicializar una lista con valores

Escribe una función `initialize_list_with_values(n, val=0)` que tome dos parámetros:

- `n` (entero) que representa la longitud de la lista que se va a crear.
- `val` (entero) que representa el valor que se utilizará para llenar la lista. Si no se proporciona `val`, se debe utilizar el valor predeterminado de `0`.

La función debe devolver una lista de longitud `n` llena con el valor especificado.

```python
def initialize_list_with_values(n, val = 0):
  return [val for x in range(n)]
```

```python
initialize_list_with_values(5, 2) # [2, 2, 2, 2, 2]
```
