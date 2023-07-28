# Import necessary libraries and create image arrays

We begin by importing the necessary libraries and creating four 10x10 image arrays using the `arange` and `reshape` functions from the NumPy library.

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import ImageGrid

im1 = np.arange(100).reshape((10, 10))
im2 = im1.T
im3 = np.flipud(im1)
im4 = np.fliplr(im2)
```
