# データの準備

このステップでは、特徴量の離散化のための合成分類データセットを準備します。scikit - learnライブラリを使って、3種類の異なるデータセット：月型、同心円型、線形に分離可能なデータを生成します。

```python
h = 0.02  # メッシュのステップサイズ

n_samples = 100
datasets = [
    make_moons(n_samples=n_samples, noise=0.2, random_state=0),
    make_circles(n_samples=n_samples, noise=0.2, factor=0.5, random_state=1),
    make_classification(
        n_samples=n_samples,
        n_features=2,
        n_redundant=0,
        n_informative=2,
        random_state=2,
        n_clusters_per_class=1,
    ),
]
```
