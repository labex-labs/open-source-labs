# 2番目の画像を作成する

`func3`関数と`imshow`関数を使って2番目の画像を作成します。

```python
Z2 = func3(X, Y)
im2 = plt.imshow(Z2, cmap=plt.cm.viridis, alpha=.9, interpolation='bilinear',
                 extent=extent)
```
