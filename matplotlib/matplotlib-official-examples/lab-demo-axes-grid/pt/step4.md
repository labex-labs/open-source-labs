# Criar uma grade de imagens 2x2 com cada imagem tendo sua própria barra de cores e uma faixa de cores diferente

Nossa grade final também será uma grade de imagens 2x2 com cada imagem tendo sua própria barra de cores, mas desta vez usaremos uma faixa de cores diferente para cada imagem. Definiremos a faixa de cores usando `vmin` e `vmax` ao plotar cada imagem.

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
