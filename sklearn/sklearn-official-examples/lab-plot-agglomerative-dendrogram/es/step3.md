# Crear el modelo

A continuación, crearemos el modelo de agrupamiento jerárquico utilizando la función `AgglomerativeClustering()` del módulo `sklearn.cluster`.

```python
model = AgglomerativeClustering(distance_threshold=0, n_clusters=None)
```
