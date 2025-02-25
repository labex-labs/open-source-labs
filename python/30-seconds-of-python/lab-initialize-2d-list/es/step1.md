# Inicializar una lista bidimensional

Escribe una función `inicializar_lista_2d(w, h, val = None)` que inicialice una lista bidimensional de un ancho y altura dados y un valor. La función debe devolver una lista de `h` filas donde cada fila es una lista con una longitud `w`, inicializada con `val`. Si no se proporciona `val`, el valor predeterminado debe ser `None`.

```python
def inicializar_lista_2d(w, h, val = None):
  return [[val for x in range(w)] for y in range(h)]
```

```python
inicializar_lista_2d(2, 2, 0) # [[0, 0], [0, 0]]
```
