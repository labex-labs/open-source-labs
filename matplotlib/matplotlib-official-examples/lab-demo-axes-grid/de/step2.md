# Erstellen eines 2x2-Bildgitters mit einer einzigen Farbskala

Unser erstes Gitter wird ein 2x2-Bildgitter mit einer einzigen Farbskala sein. Wir werden die `ImageGrid`-Funktion verwenden, um das Gitter zu erstellen und die Anzahl der Zeilen und Spalten anzugeben, die wir möchten. Wir werden auch den Ort der Farbskala angeben und `share_all` auf `True` setzen, um die Farbskala über alle Bilder zu teilen.

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
