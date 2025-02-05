# Compute Clustering

With the data and connectivity matrix defined, we can now perform hierarchical clustering. We will use scikit-learn's `AgglomerativeClustering` class to perform clustering. We will set the number of clusters to 27, which is the number of coins in the image. We will use the "ward" linkage method, which minimizes the variance of the distances between the clusters being merged. We will also pass in the connectivity matrix we created in step 2.

```python
from sklearn.cluster import AgglomerativeClustering
import time as time

print("Compute structured hierarchical clustering...")
st = time.time()
n_clusters = 27  # number of regions
ward = AgglomerativeClustering(
    n_clusters=n_clusters, linkage="ward", connectivity=connectivity
)
ward.fit(X)
label = np.reshape(ward.labels_, rescaled_coins.shape)
print(f"Elapsed time: {time.time() - st:.3f}s")
print(f"Number of pixels: {label.size}")
print(f"Number of clusters: {np.unique(label).size}")
```
