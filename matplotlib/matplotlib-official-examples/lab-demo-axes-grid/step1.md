# Import necessary libraries and data

We first need to import the necessary libraries and data to create our grid. We will use `matplotlib.pyplot` for plotting, `cbook` to get a sample data set, and `ImageGrid` to create our grid.

```python
import matplotlib.pyplot as plt
from matplotlib import cbook
from mpl_toolkits.axes_grid1 import ImageGrid

# Get sample data
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
extent = (-3, 4, -4, 3)
```
