# 組み合わせた特徴

`FeatureUnion` トランスフォーマーを使って、PCA と単変量選択から得られた特徴を組み合わせます。

```python
combined_features = FeatureUnion([("pca", pca), ("univ_select", selection)])
```
