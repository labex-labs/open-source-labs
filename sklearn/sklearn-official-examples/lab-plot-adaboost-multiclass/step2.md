# Load the Dataset

We will use the `make_gaussian_quantiles` function from `sklearn.datasets` to generate a dataset. This function generates isotropic Gaussian and adds separation between classes to make the problem harder.

```python
X, y = make_gaussian_quantiles(
    n_samples=13000, n_features=10, n_classes=3, random_state=1
)
```


