# Recursos Combinados

Combinaremos os recursos obtidos do PCA e da seleção univariada usando o transformador `FeatureUnion`.

```python
combined_features = FeatureUnion([("pca", pca), ("univ_select", selection)])
```
