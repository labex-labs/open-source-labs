# 各画像に独自のカラーバーと異なるカラーバー範囲を持つ2x2の画像のグリッドを作成する

最後のグリッドも、各画像に独自のカラーバーを持つ2x2の画像のグリッドになりますが、今回は各画像に異なるカラーバー範囲を使用します。各画像を描画する際に、`vmin`と`vmax`を使用してカラーバー範囲を設定します。

```python
# Create a grid of 2x2 images with each image having its own colorbar and a different colorbar range
grid = ImageGrid(
    fig,  # Figure object
    143,  # Location of subplot
    nrows_ncols=(2, 2),  # Number of rows and columns
    axes_pad=(0.45, 0.15),  # Padding between axes
    label_mode="1",  # Label mode
    share_all=True,  # Share colorbar across all images
    cbar_location="right",  # Location of colorbar
    cbar_mode="each",  # Colorbar mode
    cbar_size="7%",  # Size of colorbar
    cbar_pad="2%"  # Padding between colorbar and images
)

# Plot images on grid and add colorbars
limits = ((0, 1), (-2, 2), (-1.7, 1.4), (-1.5, 1))  # Different colorbar ranges
for ax, cax, vlim in zip(grid, grid.cbar_axes, limits):
    im = ax.imshow(Z, extent=extent, vmin=vlim[0], vmax=vlim[1])
    cb = cax.colorbar(im)
    cb.set_ticks((vlim[0], vlim[1]))
```
