# Generar líneas aleatorias

Generaremos 12 líneas aleatorias utilizando la biblioteca `numpy` y las graficaremos utilizando el método `plot`. Si una línea intersecta el rectángulo, su color será rojo, de lo contrario azul. Utilizaremos la clase `Path` para crear una línea y el método `intersects_bbox` para comprobar si intersecta el rectángulo.

```python
bbox = Bbox.from_bounds(left, bottom, width, height)

for i in range(12):
    vertices = (np.random.random((2, 2)) - 0.5) * 6.0
    path = Path(vertices)
    if path.intersects_bbox(bbox):
        color = 'r'
    else:
        color = 'b'
    ax.plot(vertices[:, 0], vertices[:, 1], color=color)
```
