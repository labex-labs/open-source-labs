# データの生成

`sklearn.datasets` ライブラリの `make_blobs` 関数を使ってサンプルデータを生成します。この関数は、クラスタリング用の等方性ガウスブロブを生成します。

```python
X, y = make_blobs(
    n_samples=500,
    n_features=2,
    centers=4,
    cluster_std=1,
    center_box=(-10.0, 10.0),
    shuffle=True,
    random_state=1,
)  # For reproducibility
```
