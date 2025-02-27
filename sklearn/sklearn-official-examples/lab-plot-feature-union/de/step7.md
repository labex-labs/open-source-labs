# Transformierter Datensatz

Wir werden die kombinierten Features verwenden, um den Datensatz zu transformieren.

```python
X_features = combined_features.fit(X, y).transform(X)
print("Combined space has", X_features.shape[1], "features")
```
