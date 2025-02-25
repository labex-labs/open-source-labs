# Índice del elemento mínimo

Escribe una función `min_element_index(arr)` que tome una lista de enteros `arr` como argumento y devuelva el índice del elemento con el valor mínimo en la lista.

Para resolver este problema, puedes utilizar la función `min()` para obtener el valor mínimo en la lista y luego utilizar el método `list.index()` para devolver su índice.

```python
def min_element_index(arr):
  return arr.index(min(arr))
```

```python
min_element_index([3, 5, 2, 6, 10, 7, 9]) # 2
```
