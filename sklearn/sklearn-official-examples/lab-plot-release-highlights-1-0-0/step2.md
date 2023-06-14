# Generate Data

We will generate some random data using scikit-learn's `make_regression` function. We will create 1000 samples with 10 features, and a noise level of 20.

```python
X, y = make_regression(n_samples=1000, n_features=10, noise=20)
```


