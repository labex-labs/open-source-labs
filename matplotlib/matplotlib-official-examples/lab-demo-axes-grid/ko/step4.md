# 각 이미지에 자체 컬러바와 다른 컬러바 범위를 가진 2x2 이미지 그리드 생성

마지막 그리드는 또한 각 이미지에 자체 컬러바가 있는 2x2 이미지 그리드이지만, 이번에는 각 이미지에 대해 다른 컬러바 범위를 사용합니다. 각 이미지를 플로팅할 때 `vmin` 및 `vmax`를 사용하여 컬러바 범위를 설정합니다.

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
