# 単一のカラーバー付きの 2x2 の画像のグリッドを作成する

最初のグリッドは、単一のカラーバー付きの 2x2 の画像のグリッドになります。`ImageGrid`関数を使ってグリッドを作成し、必要な行数と列数を指定します。また、カラーバーの位置を指定し、`share_all`を`True`に設定してすべての画像でカラーバーを共有します。

```python
# Create a grid of 2x2 images with a single colorbar
grid = ImageGrid(
    fig,  # Figure object
    141,  # Location of subplot
    nrows_ncols=(2, 2),  # Number of rows and columns
    axes_pad=0.0,  # Padding between axes
    label_mode="L",  # Label mode
    share_all=True,  # Share colorbar across all images
    cbar_location="top",  # Location of colorbar
    cbar_mode="single"  # Colorbar mode
)

# Plot images on grid
for ax in grid:
    im = ax.imshow(Z, extent=extent)

# Add colorbar to grid
grid.cbar_axes[0].colorbar(im)
for cax in grid.cbar_axes:
    cax.tick_params(labeltop=False)
```
