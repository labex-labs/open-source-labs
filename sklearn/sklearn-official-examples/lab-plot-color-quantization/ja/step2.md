# 画像を浮動小数点数に変換して形状を変更する

画像を浮動小数点数に変換し、2 次元の NumPy 配列に整形して、K-Means アルゴリズムで処理できるようにします。

```python
# デフォルトの 8 ビット整数コーディングではなく、浮動小数点数に変換する。
china = np.array(china, dtype=np.float64) / 255

# 画像の寸法を取得する
w, h, d = original_shape = tuple(china.shape)
assert d == 3

# 画像を 2 次元の NumPy 配列に整形する
image_array = np.reshape(china, (w * h, d))
```
