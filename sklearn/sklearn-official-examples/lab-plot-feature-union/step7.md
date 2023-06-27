# : Transformed Dataset

We will use the combined features to transform the dataset.

```python
X_features = combined_features.fit(X, y).transform(X)
print("Combined space has", X_features.shape[1], "features")
```
