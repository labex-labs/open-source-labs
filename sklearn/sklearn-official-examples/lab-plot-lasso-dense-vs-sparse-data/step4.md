# Fit Lasso to Dense Data

We fit the Lasso regression models to the dense data using Scikit-learn's `fit` function. We also time the fitting process and print the time for each Lasso model.

```python
t0 = time()
sparse_lasso.fit(X_sp, y)
print(f"Sparse Lasso done in {(time() - t0):.3f}s")

t0 = time()
dense_lasso.fit(X, y)
print(f"Dense Lasso done in {(time() - t0):.3f}s")
```


