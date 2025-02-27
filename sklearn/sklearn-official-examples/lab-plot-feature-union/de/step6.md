# Kombinierte Features

Wir werden die Features, die aus PCA und der Univariate-Selektion erhalten wurden, mit dem Transformator `FeatureUnion` kombinieren.

```python
combined_features = FeatureUnion([("pca", pca), ("univ_select", selection)])
```
