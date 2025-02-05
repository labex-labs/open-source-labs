# Data Generation

We will use the make_blobs function from the sklearn.datasets module to generate a synthetic dataset with three clusters. The dataset will consist of 750 samples with a cluster standard deviation of 0.4. We will also standardize the data using the StandardScaler from the sklearn.preprocessing module.

```python
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=750, centers=centers, cluster_std=0.4, random_state=0
)

X = StandardScaler().fit_transform(X)
```
