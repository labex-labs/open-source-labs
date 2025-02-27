# データの作成

`make_blobs` 関数を使って、ランダムな点の 2 つのクラスタを作成します。1000 個の点からなるクラスタと、100 個の点からなるクラスタを作成します。クラスタの中心はそれぞれ `[0.0, 0.0]` と `[2.0, 2.0]` になります。`clusters_std` パラメータはクラスタの標準偏差を制御します。

```python
n_samples_1 = 1000
n_samples_2 = 100
centers = [[0.0, 0.0], [2.0, 2.0]]
clusters_std = [1.5, 0.5]
X, y = make_blobs(
    n_samples=[n_samples_1, n_samples_2],
    centers=centers,
    cluster_std=clusters_std,
    random_state=0,
    shuffle=False,
)
```
