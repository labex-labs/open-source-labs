# Nearest neighbors imputation using KNNImputer

The `KNNImputer` class provides imputation for filling in missing values using the k-Nearest Neighbors approach. It finds the nearest neighbors for each sample with missing values and imputes the missing feature values based on the values of the neighbors.

```python
from sklearn.impute import KNNImputer
nan = np.nan
X = [[1, 2, nan], [3, 4, 3], [nan, 6, 5], [8, 8, 7]]
imputer = KNNImputer(n_neighbors=2)
imputed_X = imputer.fit_transform(X)
```
