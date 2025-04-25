# デモ 1 - 各軸にカラーバーを追加する

以下のコードを使用して、各軸にカラーバーを持つ 3 つの画像のグリッドを作成します。

```python
grid = ImageGrid(
    fig, 211, nrows_ncols=(1, 3), axes_pad=0.05, label_mode="1", share_all=True,
    cbar_location="top", cbar_mode="each", cbar_size="7%", cbar_pad="1%")
grid[0].set(xticks=[-2, 0], yticks=[-2, 0, 2])

for i, (ax, z) in enumerate(zip(grid, ZS)):
    im = ax.imshow(z, origin="lower", extent=extent)
    cb = ax.cax.colorbar(im)
    # Changing the colorbar ticks
    if i in [1, 2]:
        cb.set_ticks([-1, 0, 1])

for ax, im_title in zip(grid, ["Image 1", "Image 2", "Image 3"]):
    add_inner_title(ax, im_title, loc='lower left')
```

- `ImageGrid`を使用して 3 つの画像のグリッドを作成します。
- 各軸にカラーバーを追加するために、`cbar_mode`を「each」に設定します。
- すべての画像で x 軸と y 軸を共有するために、`share_all`パラメータを True に設定します。
- カラーバーを上部に配置するために、`cbar_location`パラメータを「top」に設定します。
- 最初の画像の`xticks`と`yticks`を設定します。
- 各画像をループして、`imshow`を使用して画像を軸に追加します。
- `ax.cax.colorbar`を使用して各軸にカラーバーを追加します。
- 2 番目と 3 番目の画像のカラーバーの目盛りを設定します。
- `add_inner_title`を使用して各画像にタイトルを追加します。
