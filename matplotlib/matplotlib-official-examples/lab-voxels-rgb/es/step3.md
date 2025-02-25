# Creando la esfera

Ahora crearemos una esfera en el gráfico definiendo una condición para los valores RGB que se encuentran a una cierta distancia del centro del gráfico.

```python
rc = midpoints(r)
gc = midpoints(g)
bc = midpoints(b)

sphere = (rc - 0.5)**2 + (gc - 0.5)**2 + (bc - 0.5)**2 < 0.5**2
```
