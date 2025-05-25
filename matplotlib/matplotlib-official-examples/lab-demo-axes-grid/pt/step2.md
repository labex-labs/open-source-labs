# Criar uma grade de imagens 2x2 com uma única barra de cores

Nossa primeira grade será uma grade de imagens 2x2 com uma única barra de cores. Usaremos a função `ImageGrid` para criar a grade e especificar o número de linhas e colunas que desejamos. Também especificaremos a localização da barra de cores e definiremos `share_all` como `True` para compartilhar a barra de cores em todas as imagens.

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
