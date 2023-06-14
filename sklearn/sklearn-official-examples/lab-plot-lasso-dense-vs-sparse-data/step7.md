# Train Lasso on Sparse Data

Now we train two Lasso regression models, one on the dense data and one on the sparse data. We set the alpha parameter to 0.1 and the maximum number of iterations to 10000.

```python
alpha = 0.1
sparse_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=10000)
dense_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=10000)
```


