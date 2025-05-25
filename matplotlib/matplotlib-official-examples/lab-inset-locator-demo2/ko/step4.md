# 삽입 확대 및 표시된 삽입이 있는 이미지 생성

두 번째 subplot 에서 삽입 확대 및 표시된 삽입이 있는 이미지를 생성합니다. 이는 `.mark_inset` 메서드를 사용하여 관심 영역을 표시하고 이를 삽입 축에 연결하는 방법을 보여줍니다.

```python
# Load sample data for the image
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
extent = (-3, 4, -4, 3)
Z2 = np.zeros((150, 150))
ny, nx = Z.shape
Z2[30:30+ny, 30:30+nx] = Z

# Display the image in the subplot
ax2.imshow(Z2, extent=extent, origin="lower")

# Create a zoomed inset in the upper left corner of the plot
axins2 = zoomed_inset_axes(ax2, zoom=6, loc=1)

# Display the image in the inset plot
axins2.imshow(Z2, extent=extent, origin="lower")

# Set the x and y limits of the inset plot to show the region of interest
x1, x2, y1, y2 = -1.5, -0.9, -2.5, -1.9
axins2.set_xlim(x1, x2)
axins2.set_ylim(y1, y2)

# Set the number of ticks on the inset axes
axins2.yaxis.get_major_locator().set_params(nbins=7)
axins2.xaxis.get_major_locator().set_params(nbins=7)

# Hide the tick labels on the inset axes
axins2.tick_params(labelleft=False, labelbottom=False)

# Mark the region of interest and connect it to the inset axes
mark_inset(ax2, axins2, loc1=2, loc2=4, fc="none", ec="0.5")
```
