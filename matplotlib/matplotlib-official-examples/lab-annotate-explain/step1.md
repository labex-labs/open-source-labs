# Set up the plot

First, we need to set up the plot with two subplots. We will use the `subplots` function to create a 2x2 grid of subplots, and then we will define the x and y coordinates of two points.

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, axs = plt.subplots(2, 2)
x1, y1 = 0.3, 0.3
x2, y2 = 0.7, 0.7
```
