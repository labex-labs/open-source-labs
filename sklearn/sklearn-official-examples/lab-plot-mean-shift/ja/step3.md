# MeanShift を使ってクラスタリングを計算する

次に、`sklearn.cluster` モジュールの `MeanShift` クラスを使って Mean-Shift アルゴリズムを使ってクラスタリングを計算します。各点の影響領域のサイズを表すバンド幅パラメータを自動的に検出するために、`estimate_bandwidth` 関数を使用します。

```python
bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)
ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_
```
