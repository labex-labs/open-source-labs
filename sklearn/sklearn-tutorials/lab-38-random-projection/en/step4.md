# Sparse random projection

Next, let's try another type of random projection called sparse random projection.

```python
transformer = random_projection.SparseRandomProjection()
X_new = transformer.fit_transform(X)
```

Here, we create an instance of the `SparseRandomProjection` class and apply it to our data `X` using the `fit_transform` method. The result is stored in the `X_new` variable.
