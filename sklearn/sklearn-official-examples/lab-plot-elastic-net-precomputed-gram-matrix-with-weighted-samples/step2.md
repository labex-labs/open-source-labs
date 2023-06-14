# Precomputing Gram Matrix with Weighted Samples

To fit the elastic net using the `precompute` option together with the sample weights, we must first center the design matrix and rescale it by the normalized weights prior to computing the gram matrix. We center the design matrix by subtracting the weighted average of each feature column from each row. Then, we rescale the centered design matrix by multiplying each row with the square root of the corresponding normalized weight. Finally, we compute the gram matrix by taking the dot product of the rescaled design matrix with its transpose.

```python
X_offset = np.average(X, axis=0, weights=normalized_weights)
X_centered = X - np.average(X, axis=0, weights=normalized_weights)
X_scaled = X_centered * np.sqrt(normalized_weights)[:, np.newaxis]
gram = np.dot(X_scaled.T, X_scaled)
```


