# Berechnen der Clustering mit MeanShift

Jetzt werden wir die Clustering mit dem Mean-Shift-Algorithmus mit der Klasse `MeanShift` aus dem Modul `sklearn.cluster` berechnen. Wir werden die Funktion `estimate_bandwidth` verwenden, um den Bandbreitenparameter automatisch zu erkennen, der die Größe der Einflussregion für jeden Punkt darstellt.

```python
bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)
ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_
```
