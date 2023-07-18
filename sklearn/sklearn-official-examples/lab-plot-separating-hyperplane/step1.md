# Create a Two-Class Separable Dataset

To create a two-class separable dataset, we will use the `make_blobs()` function from scikit-learn. This function generates isotropic Gaussian blobs for clustering and classification. We will create 40 samples with two centers and a random seed of 6. We will also plot the data points using `matplotlib`.

```python
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# create a two-class separable dataset
X, y = make_blobs(n_samples=40, centers=2, random_state=6)

# plot the data points
plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=plt.cm.Paired)
plt.show()
```
