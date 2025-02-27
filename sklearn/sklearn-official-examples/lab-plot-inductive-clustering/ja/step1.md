# 学習データの生成

このステップでは、クラスタリングからいくつかの学習データを生成します。scikit - learnの`make_blobs`関数を使って、異なる標準偏差と中心を持つ3つのクラスタを持つ5000個のサンプルを生成します。

```python
X, y = make_blobs(
    n_samples=5000,
    cluster_std=[1.0, 1.0, 0.5],
    centers=[(-5, -5), (0, 0), (5, 5)],
    random_state=42,
)
```
