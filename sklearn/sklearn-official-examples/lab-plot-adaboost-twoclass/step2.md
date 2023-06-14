# Construct dataset

In this step, we will create a non-linearly separable classification dataset composed of two Gaussian quantiles clusters using the `make_gaussian_quantiles` function from the `sklearn.datasets` module. We will also concatenate the two clusters and assign labels to them.

```python
X1, y1 = make_gaussian_quantiles(
    cov=2.0, n_samples=200, n_features=2, n_classes=2, random_state=1
)
X2, y2 = make_gaussian_quantiles(
    mean=(3, 3), cov=1.5, n_samples=300, n_features=2, n_classes=2, random_state=1
)
X = np.concatenate((X1, X2))
y = np.concatenate((y1, -y2 + 1))
```


