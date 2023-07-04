# Gaussian random projection

Now, let's apply Gaussian random projection to reduce the dimensionality of our data.

```python
transformer = random_projection.GaussianRandomProjection()
X_new = transformer.fit_transform(X)
```

In this step, we create an instance of the `GaussianRandomProjection` class and fit it to our data `X`. Then, we apply the transformation by calling the `fit_transform` method. The result is stored in the `X_new` variable.
