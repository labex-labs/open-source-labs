# 各カラーマップ用の BboxImage を作成する

次に、各カラーマップ用の BboxImage を作成します。まず、`plt.colormaps` メソッドを使ってすべてのカラーマップのリストを作成します。そして、カラーマップのリストをループ処理する `for` ループを作成します。各カラーマップに対して、`divmod()` メソッドを使って `ix` と `iy` の位置を計算します。次に、`Bbox.from_bounds()` メソッドを使って `Bbox` オブジェクトを作成します。`Bbox.from_bounds()` メソッドに `ix`、`iy`、`dx`、および `dy` の値を渡してバウンディングボックスを作成します。そして、`Bbox` オブジェクトと `ax2.transAxes` オブジェクトを使って `TransformedBbox` オブジェクトを作成します。最後に、`add_artist()` メソッドを使って `BboxImage` オブジェクトを作成します。`BboxImage` コンストラクタに `TransformedBbox` オブジェクトを渡して、カラーマップ付きの画像を作成します。

```python
cmap_names = sorted(m for m in plt.colormaps if not m.endswith("_r"))

ncol = 2
nrow = len(cmap_names) // ncol + 1

xpad_fraction = 0.3
dx = 1 / (ncol + xpad_fraction * (ncol - 1))

ypad_fraction = 0.3
dy = 1 / (nrow + ypad_fraction * (nrow - 1))

for i, cmap_name in enumerate(cmap_names):
    ix, iy = divmod(i, nrow)
    bbox0 = Bbox.from_bounds(ix*dx*(1+xpad_fraction),
                             1 - iy*dy*(1+ypad_fraction) - dy,
                             dx, dy)
    bbox = TransformedBbox(bbox0, ax2.transAxes)
    ax2.add_artist(
        BboxImage(bbox, cmap=cmap_name, data=np.arange(256).reshape((1, -1))))
```
