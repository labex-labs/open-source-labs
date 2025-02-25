# ImageGridに画像を表示する

最後に、`imshow`関数と`zip`関数を使用してImageGridに画像を表示し、グリッド内の軸を反復処理します。

```python
for ax, im in zip(grid, [im1, im2, im3]):
    ax.imshow(im, origin="lower", vmin=vmin, vmax=vmax)

plt.show()
```
