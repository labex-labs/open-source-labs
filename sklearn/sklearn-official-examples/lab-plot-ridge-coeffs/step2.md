# Generate random data

We will generate random data with `make_regression` function from scikit-learn. We will set `n_samples` to 10, `n_features` to 10, and `random_state` to 1. This function will return our input features X, our target variable y, and the true coefficient values w.

```python
X, y, w = make_regression(
    n_samples=10, n_features=10, coef=True, random_state=1, bias=3.5
)
```
