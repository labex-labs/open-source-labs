# Adicionar uma Seta de Orientação

Você pode adicionar uma seta de orientação à elipse plotando um marcador no ponto final do eixo menor. Você pode usar o método `get_co_vertices()` para obter as coordenadas dos vértices da elipse. Em seguida, você pode usar a classe `Affine2D()` para rotacionar o marcador para corresponder ao ângulo da elipse.

```python
from matplotlib.markers import MarkerStyle
from matplotlib.transforms import Affine2D

# Plot an arrow marker at the end point of minor axis
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
