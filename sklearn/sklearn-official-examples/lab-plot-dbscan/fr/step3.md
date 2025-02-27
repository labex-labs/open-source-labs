# Calcul de DBSCAN

Nous utiliserons la classe DBSCAN du module sklearn.cluster pour calculer les groupes. Nous définirons le paramètre eps sur 0,3 et le paramètre min_samples sur 10. Nous pouvons accéder aux étiquettes attribuées par DBSCAN à l'aide de l'attribut labels. Les échantillons bruyants sont donnés l'étiquette -1. Nous calculerons également le nombre de groupes et le nombre de points de bruit.

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
