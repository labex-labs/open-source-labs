# 각 이미지에 자체 컬러바가 있는 2x2 이미지 그리드 생성

다음 그리드는 각 이미지에 자체 컬러바가 있는 2x2 이미지 그리드가 될 것입니다. `ImageGrid` 함수를 다시 사용하지만, 이번에는 `cbar_mode`를 `"each"`로 설정하여 각 이미지가 자체 컬러바를 가져야 함을 지정합니다.

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
