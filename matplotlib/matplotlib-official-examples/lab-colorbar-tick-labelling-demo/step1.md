# Import necessary libraries and fix random state

First, we need to import the necessary libraries and fix the random state for reproducibility. We will use `numpy` to generate some random data, `matplotlib.pyplot` for creating visualizations, and `cm` from `matplotlib` for defining the color maps.

```python
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn

from matplotlib import cm

# Fixing random state for reproducibility
np.random.seed(19680801)
```
