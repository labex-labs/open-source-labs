# Marking imputed values using MissingIndicator

The `MissingIndicator` transformer is useful for indicating the presence of missing values in a dataset. It can be used in conjunction with imputation to preserve information about which values were imputed. This transformer returns a binary matrix indicating the presence of missing values in the dataset.

```python
from sklearn.impute import MissingIndicator
X = np.array([[-1, -1, 1, 3], [4, -1, 0, -1], [8, -1, 1, 0]])
indicator = MissingIndicator()
mask_missing_values_only = indicator.fit_transform(X)
```
