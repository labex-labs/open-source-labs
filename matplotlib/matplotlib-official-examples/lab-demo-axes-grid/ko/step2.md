# 단일 컬러바를 가진 2x2 이미지 그리드 생성

첫 번째 그리드는 단일 컬러바를 가진 2x2 이미지 그리드가 될 것입니다. `ImageGrid` 함수를 사용하여 그리드를 생성하고 원하는 행과 열의 수를 지정합니다. 또한 컬러바의 위치를 지정하고 모든 이미지에서 컬러바를 공유하기 위해 `share_all`을 `True`로 설정합니다.

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
