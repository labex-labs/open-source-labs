# Características Combinadas

Combinaremos las características obtenidas a partir del PCA y la selección univariada utilizando el transformador `FeatureUnion`.

```python
combined_features = FeatureUnion([("pca", pca), ("univ_select", selection)])
```
