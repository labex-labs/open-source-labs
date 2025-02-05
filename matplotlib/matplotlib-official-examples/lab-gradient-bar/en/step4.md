# Define the gradient bar function

Next, we need to define a function that will create a gradient bar. This function will take in the axes object, the x and y coordinates of the bar, the width of the bar, and the bottom position of the bar. The function will then create a gradient image for each bar and return it.

```python
def gradient_bar(ax, x, y, width=0.5, bottom=0):
    for left, top in zip(x, y):
        right = left + width
        gradient_image(ax, extent=(left, right, bottom, top),
                       cmap=plt.cm.Blues_r, cmap_range=(0, 0.8))
```
