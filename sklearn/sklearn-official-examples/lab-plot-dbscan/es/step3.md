# Calcular DBSCAN

Usaremos la clase DBSCAN del módulo sklearn.cluster para calcular los clusters. Estableceremos el parámetro eps en 0.3 y el parámetro min_samples en 10. Podemos acceder a las etiquetas asignadas por DBSCAN usando el atributo labels. Las muestras ruidosas se les da la etiqueta -1. También calcularemos el número de clusters y el número de puntos de ruido.

```python
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics

db = DBSCAN(eps=0.3, min_samples=10).fit(X)
labels = db.labels_

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print("Estimated number of clusters: %d" % n_clusters_)
print("Estimated number of noise points: %d" % n_noise_)
```
