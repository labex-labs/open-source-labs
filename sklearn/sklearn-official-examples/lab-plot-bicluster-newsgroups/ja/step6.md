# スペクトラル共クラスタリングアルゴリズムを用いた二部クラスタリング

共クラスタを定義し、データに適合させることで、スペクトラル共クラスタリングアルゴリズムを使って二部クラスタリングを行います。

```python
cocluster = SpectralCoclustering(
    n_clusters=len(categories), svd_method="arpack", random_state=0
)
cocluster.fit(X)
y_cocluster = cocluster.row_labels_
```
