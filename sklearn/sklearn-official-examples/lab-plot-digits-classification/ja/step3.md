# データセットの準備

画像をフラットにする必要があります。これにより、グレースケール値の各 2 次元配列を形状 `(8, 8)` から形状 `(64,)` に変換します。これにより、形状 `(n_samples, n_features)` のデータセットが得られます。ここで、`n_samples` は画像の数であり、`n_features` は各画像のピクセルの総数です。

```python
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))
```
