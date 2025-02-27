# クラスタ数とアルゴリズムの定義

このステップでは、KMeans と BisectingKMeans のクラスタ中心数を定義します。また、比較するアルゴリズムも定義します。

```python
n_clusters_list = [4, 8, 16]
clustering_algorithms = {
    "Bisecting K-Means": BisectingKMeans,
    "K-Means": KMeans,
}
```
