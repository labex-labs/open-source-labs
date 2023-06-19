# Create a Colormap from a List of Colors

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
