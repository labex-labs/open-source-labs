# Transponer una matriz

Escribe una función llamada `transpose(lst)` que tome una lista bidimensional como argumento y devuelva la traspuesta de la lista dada.

Sigue estos pasos para resolver el problema:

- Utiliza `*lst` para obtener la lista proporcionada como tuplas.
- Utiliza `zip()` en combinación con `list()` para crear la traspuesta de la lista bidimensional dada.

```python
def transpose(lst):
  return list(zip(*lst))
```

```python
transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# [(1, 4, 7, 10), (2, 5, 8, 11), (3, 6, 9, 12)]
```
