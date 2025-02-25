# Erstellen eines 2x2-Bildgitters, wobei jedes Bild seine eigene Farbskala hat

Unser nächstes Gitter wird ein 2x2-Bildgitter sein, wobei jedes Bild seine eigene Farbskala hat. Wir werden erneut die `ImageGrid`-Funktion verwenden, aber diesmal werden wir `cbar_mode` auf `"each"` setzen, um anzugeben, dass jedes Bild seine eigene Farbskala haben soll.

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
