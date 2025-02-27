# 画像を浮動小数点数に変換して形状を変更する

画像を浮動小数点数に変換し、2次元のNumPy配列に整形して、K-Meansアルゴリズムで処理できるようにします。

```python
# デフォルトの8ビット整数コーディングではなく、浮動小数点数に変換する。
china = np.array(china, dtype=np.float64) / 255

# 画像の寸法を取得する
w, h, d = original_shape = tuple(china.shape)
assert d == 3

# 画像を2次元のNumPy配列に整形する
image_array = np.reshape(china, (w * h, d))
```
