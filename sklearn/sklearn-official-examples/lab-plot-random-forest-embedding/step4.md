# Visualize Result After Dimensionality Reduction using Truncated SVD

In this step, we will visualize the result after dimensionality reduction using truncated SVD.

```python
svd = TruncatedSVD(n_components=2)
X_reduced = svd.fit_transform(X_transformed)
```


