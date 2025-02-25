# 各画像に独自のカラーバーを持つ2x2の画像のグリッドを作成する

次のグリッドは、各画像に独自のカラーバーを持つ2x2の画像のグリッドになります。再び`ImageGrid`関数を使いますが、今回は各画像に独自のカラーバーを持つようにするために`cbar_mode`を`"each"`に設定します。

```python
# Create a grid of 2x2 images with each image having its own colorbar
grid = ImageGrid(
    fig,  # Figure object
    142,  # Location of subplot
    nrows_ncols=(2, 2),  # Number of rows and columns
    axes_pad=0.1,  # Padding between axes
    label_mode="1",  # Label mode
    share_all=True,  # Share colorbar across all images
    cbar_location="top",  # Location of colorbar
    cbar_mode="each",  # Colorbar mode
    cbar_size="7%",  # Size of colorbar
    cbar_pad="2%"  # Padding between colorbar and images
)

# Plot images on grid and add colorbars
for ax, cax in zip(grid, grid.cbar_axes):
    im = ax.imshow(Z, extent=extent)
    cax.colorbar(im)
    cax.tick_params(labeltop=False)
```
