# Import necessary libraries and set up plot

First, we need to import the necessary libraries and set up the plot. We will be using `matplotlib.pyplot` and `numpy`. We will also create a figure and an axis object to plot our data on.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import FancyArrowPatch

fig, ax = plt.subplots()
ax.set(xlim=(0, 6), ylim=(-1, 5))
ax.set_title("Orientation of the bracket arrows relative to angleA and angleB")
```
