# 数字のデータセットを読み込んで可視化する

8x8 ピクセルの数字の画像から構成される数字のデータセットを読み込みます。最初の 4 つの画像とそれに対応するラベルを可視化するために、`matplotlib` の `imshow()` メソッドを使用します。

```python
digits = datasets.load_digits()

_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, label in zip(axes, digits.images, digits.target):
    ax.set_axis_off()
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    ax.set_title("Training: %i" % label)
```
