# Scalability and Stability Improvements to KMeans

The KMeans estimator was entirely reworked in scikit-learn 0.23 to be faster and more stable. In addition, the Elkan algorithm is now compatible with sparse matrices. The estimator uses OpenMP based parallelism instead of relying on joblib, so the n_jobs parameter has no effect anymore.

```python
import scipy
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import completeness_score

# create a dataset
rng = np.random.RandomState(0)
X, y = make_blobs(random_state=rng)
X = scipy.sparse.csr_matrix(X)
X_train, X_test, _, y_test = train_test_split(X, y, random_state=rng)

# create and fit a KMeans model
kmeans = KMeans(n_init="auto").fit(X_train)

# calculate the completeness score
print(completeness_score(kmeans.predict(X_test), y_test))
```
