# Use PCA to project the dataset

PCA is used to project the dataset onto a new space that preserves most of its original variation.

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)

X_test_pca = pca.fit(X_train).transform(X_test)
```


