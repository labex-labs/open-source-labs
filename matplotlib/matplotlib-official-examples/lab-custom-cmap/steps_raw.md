# Creating a Custom Colormap with Matplotlib

## Introduction

Matplotlib is a popular data visualization library in Python. It provides a wide range of colormaps that can be used to represent data. However, sometimes the default colormaps do not meet our needs. In such cases, we can create custom colormaps that suit our requirements. In this lab, we will learn how to create custom colormaps using Matplotlib.

## Steps

### Step 1: Create a Colormap from a List of Colors

The `.LinearSegmentedColormap.from_list` method allows us to create a colormap from a list of colors. We need to pass a list of RGB tuples that define the mixture of colors from 0 to 1.

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# define a list of colors
colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]  # R -> G -> B
# define the number of bins
n_bins = 10
# define the name of the colormap
cmap_name = 'my_list'

# create the colormap
cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)
```

### Step 2: Create a Custom Colormap

We can create a custom mapping for a colormap by creating a dictionary that specifies how the RGB channels change from one end of the colormap to the other.

```python
cdict = {
    'red': (
        (0.0, 0.0, 0.0),
        (0.5, 0.0, 0.1),
        (1.0, 1.0, 1.0),
    ),
    'green': (
        (0.0, 0.0, 0.0),
        (1.0, 0.0, 0.0),
    ),
    'blue': (
        (0.0, 0.0, 1.0),
        (0.5, 0.1, 0.0),
        (1.0, 0.0, 0.0),
    )
}

# create the colormap
blue_red = LinearSegmentedColormap('BlueRed', cdict)
```

### Step 3: Register the Custom Colormap

We can register the custom colormap by using the `.register_cmap` method of Matplotlib's `cm` module.

```python
import matplotlib.cm as cm
cm.register_cmap(cmap=blue_red)
```

### Step 4: Use the Custom Colormap

We can use the custom colormap in our visualizations by passing the name of the colormap to the `cmap` parameter of Matplotlib's plotting functions.

```python
# create some data
x = np.arange(0, np.pi, 0.1)
y = np.arange(0, 2 * np.pi, 0.1)
X, Y = np.meshgrid(x, y)
Z = np.cos(X) * np.sin(Y) * 10

# plot the data using the custom colormap
plt.imshow(Z, cmap='BlueRed')
plt.colorbar()
plt.show()
```

## Summary

In this lab, we learned how to create custom colormaps using Matplotlib. We saw how to create a colormap from a list of colors, create a custom colormap using a dictionary, register the custom colormap, and use the custom colormap in our visualizations. By creating custom colormaps, we can represent data in a way that is more visually appealing and informative.
