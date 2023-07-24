# Discretize the Input Feature

In this step, we will use the KBinsDiscretizer class to discretize the input feature. We will create 10 bins and use one-hot encoding to transform the data.

```python
enc = KBinsDiscretizer(n_bins=10, encode="onehot")
X_binned = enc.fit_transform(X)
```
