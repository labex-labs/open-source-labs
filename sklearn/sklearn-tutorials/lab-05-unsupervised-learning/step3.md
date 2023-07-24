# Vector Quantization

One application of clustering is vector quantization, where we use clustering to choose a small number of exemplars to compress information. For example, we can use clustering to posterize an image:

```python
import scipy as sp
from sklearn import cluster, datasets

# Load a sample image
face = sp.face(gray=True)
X = face.reshape((-1, 1))

# Perform K-means clustering
k_means = cluster.KMeans(n_clusters=5, n_init=1)
k_means.fit(X)

# Compress the image using cluster centers
values = k_means.cluster_centers_.squeeze()
labels = k_means.labels_
face_compressed = np.choose(labels, values)
face_compressed.shape = face.shape
```
