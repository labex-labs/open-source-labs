# Inicializar una lista bidimensional

## Problema

Escribe una función `inicializar_lista_2d(w, h, val=None)` que inicialice una lista bidimensional de ancho y altura dados y valor. La función debe devolver una lista de `h` filas donde cada fila es una lista con longitud `w`, inicializada con `val`. Si no se proporciona `val`, el valor predeterminado debe ser `None`.

## Ejemplo

```python
inicializar_lista_2d(2, 2, 0) # [[0, 0], [0, 0]]
inicializar_lista_2d(3, 3, "x") # [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]]
inicializar_lista_2d(2, 3) # [[None, None], [None, None], [None, None]]
```
