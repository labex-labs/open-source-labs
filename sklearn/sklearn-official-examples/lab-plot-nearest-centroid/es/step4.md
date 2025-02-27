# Crear y ajustar el clasificador

Creamos una instancia del clasificador Nearest Centroid con un valor de contracción de 0,2 y ajustamos los datos.

```python
clf = NearestCentroid(shrink_threshold=0.2)
clf.fit(X, y)
```
