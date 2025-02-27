# サンプルデータを生成する

`sklearn.datasets` モジュールの `make_blobs` 関数を使ってサンプルデータセットを生成します。`make_blobs` 関数は、n次元空間の点のデータセットを生成し、各点はk個のクラスタの1つに属します。ここでは、2次元空間に300個の点からなるデータセットを生成し、3つのクラスタと標準偏差0.5で生成します。

```python
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=300, centers=centers, cluster_std=0.5, random_state=0
)
```
