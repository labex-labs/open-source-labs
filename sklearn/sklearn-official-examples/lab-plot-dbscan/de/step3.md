# DBSCAN berechnen

Wir werden die DBSCAN-Klasse aus dem sklearn.cluster-Modul verwenden, um die Cluster zu berechnen. Wir werden den eps-Parameter auf 0,3 und den min_samples-Parameter auf 10 setzen. Wir können die von DBSCAN zugewiesenen Labels über das labels-Attribut zugreifen. Rauschproben erhalten das Label -1. Wir werden auch die Anzahl der Cluster und die Anzahl der Rauschpunkte berechnen.

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
