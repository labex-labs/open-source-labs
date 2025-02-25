# Crear una BboxImage con Texto

Comenzamos creando una BboxImage con Texto. Creamos un objeto `text` con el método `text()` y lo agregamos al objeto `ax1`. Luego creamos un objeto `BboxImage` utilizando el método `add_artist()`. Pasamos el método `get_window_extent` del objeto `text` al constructor de `BboxImage` para obtener el cuadro delimitador del texto. También pasamos una matriz unidimensional de forma (1, 256) al parámetro `data` del constructor de `BboxImage` para crear una imagen.

```python
fig, (ax1, ax2) = plt.subplots(ncols=2)

txt = ax1.text(0.5, 0.5, "test", size=30, ha="center", color="w")
ax1.add_artist(
    BboxImage(txt.get_window_extent, data=np.arange(256).reshape((1, -1))))
```
