# データの生成

このステップでは、`n_samples` 個のサンプルと `n_features` 個の特徴を持つランダムなデータセットを生成します。また、データセットにいくつかのアウトライアを追加します。

```python
n_samples = 80
n_features = 5

# ランダムなデータセットを生成する
rng = np.random.RandomState(42)
X = rng.randn(n_samples, n_features)

# データセットにアウトライアを追加する
n_outliers = 20
outliers_index = rng.permutation(n_samples)[:n_outliers]
outliers_offset = 10.0 * (
    np.random.randint(2, size=(n_outliers, n_features)) - 0.5
)
X[outliers_index] += outliers_offset
```
