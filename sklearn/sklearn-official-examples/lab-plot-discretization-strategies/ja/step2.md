# データセットの作成

可視化の目的で 3 つのデータセットを作成します。最初のデータセットは、両次元ともに - 3 から 3 の一様分布からの 200 個のサンプルのランダムなセットです。2 番目のデータセットは、`sklearn.datasets`からの`make_blobs`関数を使用して生成された 200 個のサンプルのセットです。3 番目のデータセットも`make_blobs`関数を使用して生成されます。

```python
n_samples = 200
centers_0 = np.array([[0, 0], [0, 5], [2, 4], [8, 8]])
centers_1 = np.array([[0, 0], [3, 1]])

X_list = [
    np.random.RandomState(42).uniform(-3, 3, size=(n_samples, 2)),
    make_blobs(
        n_samples=[n_samples // 10, n_samples * 4 // 10, n_samples // 10, n_samples * 4 // 10],
        cluster_std=0.5,
        centers=centers_0,
        random_state=42,
    )[0],
    make_blobs(
        n_samples=[n_samples // 5, n_samples * 4 // 5],
        cluster_std=0.5,
        centers=centers_1,
        random_state=42,
    )[0],
]
```
