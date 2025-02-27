# サンプルデータを生成する

次に、`sklearn.datasets` モジュールの `make_blobs` 関数を使ってサンプルデータを生成します。中心が `[[1, 1], [-1, -1], [1, -1]]` で標準偏差が 0.6 の 3 つのクラスタを持つ 10,000 個のサンプルからなるデータセットを作成します。

```python
centers = [[1, 1], [-1, -1], [1, -1]]
X, _ = make_blobs(n_samples=10000, centers=centers, cluster_std=0.6)
```
