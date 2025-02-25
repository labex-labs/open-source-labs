# Ocultar triángulos no deseados

Ocultaremos los triángulos no deseados calculando la media de las coordenadas x e y de los vértices de cada triángulo y comparándola con el radio mínimo.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
