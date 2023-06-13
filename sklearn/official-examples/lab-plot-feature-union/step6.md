# Step 3.3: Combined Features

We will combine the features obtained from PCA and univariate selection using the `FeatureUnion` transformer.

```python
combined_features = FeatureUnion([("pca", pca), ("univ_select", selection)])
```

#
