# Load Dataset

We will load the California housing dataset using the scikit-learn `fetch_california_housing` function. This dataset consists of 20,640 samples and 8 features.

```python
from sklearn.datasets import fetch_california_housing

X, y = fetch_california_housing(return_X_y=True, as_frame=True)
n_samples, n_features = X.shape

print(f"The dataset consists of {n_samples} samples and {n_features} features")
```


