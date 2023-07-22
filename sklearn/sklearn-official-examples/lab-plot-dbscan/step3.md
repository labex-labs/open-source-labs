# Compute DBSCAN

We will use the DBSCAN class from the sklearn.cluster module to compute the clusters. We will set the eps parameter to 0.3 and the min*samples parameter to 10. We can access the labels assigned by DBSCAN using the labels* attribute. Noisy samples are given the label -1. We will also calculate the number of clusters and the number of noise points.

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
