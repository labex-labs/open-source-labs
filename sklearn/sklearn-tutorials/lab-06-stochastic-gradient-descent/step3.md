# Preprocess Data

Before applying SGD, it is often beneficial to preprocess the data. In this case, we will standardize the features using scikit-learn's StandardScaler.

```python
scaler = StandardScaler()
X = scaler.fit_transform(X)
```
