# Inverse transform

Random projection transformers have an option to compute the inverse of the projection matrix. Let's explore this feature by applying the inverse transform to our projected data.

```python
transformer = random_projection.SparseRandomProjection(compute_inverse_components=True)
X_new = transformer.fit_transform(X)

# Compute the inverse transform
X_new_inversed = transformer.inverse_transform(X_new)
```

In this step, we create an instance of the `SparseRandomProjection` class with the `compute_inverse_components` parameter set to `True`. Then, we fit the transformer to our data `X` and apply the transformation. Finally, we compute the inverse transform by calling the `inverse_transform` method on the projected data `X_new`.
