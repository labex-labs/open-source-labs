# Create a GridSearchCV object and fit data

We will create a `GridSearchCV` object using the pipeline and parameter grid we defined in the previous step. We will then fit the data to the object.

```python
grid = GridSearchCV(pipe, n_jobs=1, param_grid=param_grid)
grid.fit(X, y)
```


