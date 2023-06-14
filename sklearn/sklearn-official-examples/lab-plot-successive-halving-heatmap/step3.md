# Perform Successive Halving

We will now perform parameter search using Successive Halving on the same SVC model and dataset used in Step 2.

```python
tic = time()
gsh = HalvingGridSearchCV(
    estimator=clf, param_grid=param_grid, factor=2, random_state=rng
)
gsh.fit(X, y)
gsh_time = time() - tic
```


