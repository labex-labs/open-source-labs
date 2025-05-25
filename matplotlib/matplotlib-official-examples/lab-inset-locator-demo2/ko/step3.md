# 크기 막대가 있는 확대된 삽입 생성

첫 번째 subplot 에서 크기 막대가 있는 확대된 삽입을 생성합니다. 이는 `.zoomed_inset_axes` 메서드를 사용하여 확대된 삽입을 만드는 방법을 보여줍니다.

```python
# Set the aspect ratio of the plot to 1
ax.set_aspect(1)

# Create a zoomed inset in the upper right corner of the plot
axins = zoomed_inset_axes(ax, zoom=0.5, loc='upper right')

# Set the number of ticks on the inset axes
axins.yaxis.get_major_locator().set_params(nbins=7)
axins.xaxis.get_major_locator().set_params(nbins=7)

# Hide the tick labels on the inset axes
axins.tick_params(labelleft=False, labelbottom=False)

# Define a function to add a size bar to the plot
def add_sizebar(ax, size):
    asb = AnchoredSizeBar(ax.transData,
                          size,
                          str(size),
                          loc=8,
                          pad=0.1, borderpad=0.5, sep=5,
                          frameon=False)
    ax.add_artist(asb)

# Add a size bar to the main plot and the inset plot
add_sizebar(ax, 0.5)
add_sizebar(axins, 0.5)
```
