# Create a grid of 2x2 images with a single colorbar

Our first grid will be a 2x2 grid of images with a single colorbar. We will use the `ImageGrid` function to create the grid and specify the number of rows and columns we want. We will also specify the location of the colorbar and set `share_all` to `True` to share the colorbar across all images.

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
