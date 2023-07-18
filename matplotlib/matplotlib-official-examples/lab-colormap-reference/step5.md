# Creating Custom Color Maps

Matplotlib also provides the ability to create custom color maps. This can be useful when the built-in color maps do not provide the desired representation of the data.

```python
import matplotlib.colors as mcolors

# Define a list of colors and their corresponding values
colors = [(0, 'red'), (0.5, 'green'), (1, 'blue')]

# Create a LinearSegmentedColormap object from the list of colors
cmap = mcolors.LinearSegmentedColormap.from_list('my_cmap', colors)
```
