# Crear segmentos de línea

Crearemos un conjunto de segmentos de línea para poder colorearlos individualmente. Usaremos la función `concatenate` de numpy para concatenar dos matrices `points[:-1]` y `points[1:]` a lo largo del segundo eje. Luego, redimensionaremos la matriz resultante a una matriz N x 1 x 2 para que podamos apilar fácilmente los puntos para obtener los segmentos. La matriz de segmentos para la recopilación de líneas debe ser (numlines) x (puntos por línea) x 2 (para x e y).

```python
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
```
