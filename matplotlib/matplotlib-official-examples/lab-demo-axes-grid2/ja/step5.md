# デモ2 - 共有のカラーバー

以下のコードを使用して、共有のカラーバーを持つ3つの画像のグリッドを作成します。

```python
grid2 = ImageGrid(
    fig, 212, nrows_ncols=(1, 3), axes_pad=0.05, label_mode="1", share_all=True,
    cbar_location="right", cbar_mode="single", cbar_size="10%", cbar_pad=0.05)
grid2[0].set(xlabel="X", ylabel="Y", xticks=[-2, 0], yticks=[-2, 0, 2])

clim = (np.min(ZS), np.max(ZS))
for ax, z in zip(grid2, ZS):
    im = ax.imshow(z, clim=clim, origin="lower", extent=extent)

# With cbar_mode="single", cax attribute of all axes are identical.
ax.cax.colorbar(im)

for ax, im_title in zip(grid2, ["(a)", "(b)", "(c)"]):
    add_inner_title(ax, im_title, loc='upper left')
```

- `ImageGrid`を使用して3つの画像のグリッドを作成します。
- 共有のカラーバーを追加するために、`cbar_mode`を「single」に設定します。
- すべての画像でx軸とy軸を共有するために、`share_all`パラメータをTrueに設定します。
- カラーバーを右側に配置するために、`cbar_location`パラメータを「right」に設定します。
- 最初の画像の`xticks`と`yticks`を設定します。
- 各画像をループして、`imshow`を使用して画像を軸に追加します。
- すべての画像が同じ色スケールを使用するように、`clim`パラメータを設定します。
- `ax.cax.colorbar`を使用して軸に共有のカラーバーを追加します。
- `add_inner_title`を使用して各画像にタイトルを追加します。
