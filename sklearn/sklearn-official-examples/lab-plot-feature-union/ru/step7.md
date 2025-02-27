# Преобразованный датасет

Мы будем использовать объединенные признаки для преобразования датасета.

```python
X_features = combined_features.fit(X, y).transform(X)
print("Combined space has", X_features.shape[1], "features")
```
