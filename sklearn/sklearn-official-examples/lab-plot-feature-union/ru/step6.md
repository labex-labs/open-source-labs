# Объединенные признаки

Мы объединим признаки, полученные с использованием PCA и одномерного отбора, с помощью трансформера `FeatureUnion`.

```python
combined_features = FeatureUnion([("pca", pca), ("univ_select", selection)])
```
