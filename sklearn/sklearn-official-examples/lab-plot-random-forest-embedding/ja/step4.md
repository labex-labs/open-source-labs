# トランケートされたSVDを使った次元削減後の結果を可視化する

このステップでは、トランケートされたSVDを使った次元削減後の結果を可視化します。

```python
svd = TruncatedSVD(n_components=2)
X_reduced = svd.fit_transform(X_transformed)
```
