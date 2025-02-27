# Die Daten generieren

Wir beginnen mit der Erzeugung der Blobs von Daten, die gruppiert werden sollen.

```python
import numpy as np
from sklearn.datasets import make_blobs

np.random.seed(0)

batch_size = 45
centers = [[1, 1], [-1, -1], [1, -1]]
n_clusters = len(centers)
X, labels_true = make_blobs(n_samples=3000, centers=centers, cluster_std=0.7)
```
