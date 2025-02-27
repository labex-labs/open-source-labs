# Calcular el agrupamiento con MeanShift

Ahora calcularemos el agrupamiento utilizando el algoritmo Mean-Shift con la clase `MeanShift` del módulo `sklearn.cluster`. Utilizaremos la función `estimate_bandwidth` para detectar automáticamente el parámetro de ancho de banda, que representa el tamaño de la región de influencia para cada punto.

```python
bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)
ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_
```
