# Creating a Simple Color Map

To create a simple color map, we can use the `ListedColormap` class from the `matplotlib.colors` module. This class takes a list of colors and creates a color map from them.

```python
import matplotlib.colors as mcolors

# Define a list of colors
colors = ['red', 'green', 'blue']

# Create a ListedColormap object from the list of colors
cmap = mcolors.ListedColormap(colors)
```
