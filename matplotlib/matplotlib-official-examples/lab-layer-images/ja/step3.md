# 範囲を定義して最初の画像を作成する

範囲を定義し、`imshow`関数を使って最初の画像を作成します。

```python
extent = np.min(x), np.max(x), np.min(y), np.max(y)
Z1 = np.add.outer(range(8), range(8)) % 2  # チェス盤模様
im1 = plt.imshow(Z1, cmap=plt.cm.gray, interpolation='nearest',
                 extent=extent)
```
