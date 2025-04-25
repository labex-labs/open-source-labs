# OPTICS クラスタリングアルゴリズムを実行する

次に、生成したデータに対して OPTICS クラスタリングアルゴリズムを実行します。この例では、`min_samples=50`、`xi=0.05`、および`min_cluster_size=0.05`を設定します。

```python
clust = OPTICS(min_samples=50, xi=0.05, min_cluster_size=0.05)
clust.fit(X)
```
