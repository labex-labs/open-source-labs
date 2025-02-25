# Agregar una flecha de orientación

Puede agregar una flecha de orientación a la elipse trazando un marcador en el punto final del eje menor. Puede utilizar el método `get_co_vertices()` para obtener las coordenadas de los vértices de la elipse. Luego, puede utilizar la clase `Affine2D()` para rotar el marcador para que coincida con el ángulo de la elipse.

```python
from matplotlib.markers import MarkerStyle
from matplotlib.transforms import Affine2D

# Trazar un marcador de flecha en el punto final del eje menor
vertices = ellipse.get_co_vertices()
t = Affine2D().rotate_deg(ellipse.angle)
ax.plot(
    vertices[0][0],
    vertices[0][1],
    color="b",
    marker=MarkerStyle(">", "full", t),
    markersize=10
)
```
