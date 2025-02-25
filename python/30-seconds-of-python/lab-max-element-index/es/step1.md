# Índice del Elemento Máximo

Escribe una función `max_element_index(arr)` que tome una lista `arr` como argumento y devuelva el índice del elemento con el valor máximo. Si hay múltiples elementos con el valor máximo, devuelve el índice de la primera aparición.

Para resolver este problema, puedes seguir estos pasos:

1. Utiliza la función `max()` incorporada para encontrar el valor máximo en la lista.
2. Utiliza la función `list.index()` incorporada para encontrar el índice de la primera aparición del valor máximo en la lista.
3. Devuelve el índice.

```python
def max_element_index(arr):
  return arr.index(max(arr))
```

```python
max_element_index([5, 8, 9, 7, 10, 3, 0]) # 4
```
