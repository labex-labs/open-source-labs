# Train Lasso on Dense Data

Now we train two Lasso regression models, one on the dense data and one on the sparse data. We set the alpha parameter to 1 and the maximum number of iterations to 1000.

```python
alpha = 1
sparse_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=1000)
dense_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=1000)
```
