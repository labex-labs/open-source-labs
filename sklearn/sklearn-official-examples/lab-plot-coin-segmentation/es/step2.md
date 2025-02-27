# Convertir la imagen en un gráfico con el valor del gradiente en los bordes

Convertiremos la imagen en un gráfico con el valor del gradiente en los bordes. Entre menor sea beta, más independiente será la segmentación de la imagen real. Para beta = 1, la segmentación es cercana a una voronoi.

```python
# Convertir la imagen en un gráfico con el valor del gradiente en los
# bordes.
grafica = imagen.img_to_graph(monedas_redimensionadas)

# Tomar una función decreciente del gradiente: una exponencial
beta = 10
eps = 1e-6
grafica.data = np.exp(-beta * grafica.data / grafica.data.std()) + eps
```
