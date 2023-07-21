# Create the Figure and Outer Grid

Next, we will create the figure and the outer grid using the `add_gridspec` function. We will create a 4x4 grid with no spacing between the subplots.

```python
fig = plt.figure(figsize=(8, 8))
outer_grid = fig.add_gridspec(4, 4, wspace=0, hspace=0)
```
