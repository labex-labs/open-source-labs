# Create a grid of 2x2 images with each image having its own colorbar

Our next grid will be a 2x2 grid of images with each image having its own colorbar. We will use the `ImageGrid` function again, but this time we will set `cbar_mode` to `"each"` to specify that each image should have its own colorbar.

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
