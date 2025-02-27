# Caractéristiques combinées

Nous allons combiner les caractéristiques obtenues à partir de la PCA et de la sélection univariée à l'aide du transformateur `FeatureUnion`.

```python
combined_features = FeatureUnion([("pca", pca), ("univ_select", selection)])
```
