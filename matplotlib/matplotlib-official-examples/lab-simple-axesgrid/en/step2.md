# Create a figure and an ImageGrid object

Next, we create a `figure` object using the `plt.figure` function and pass in the `figsize` argument to set the size of the figure. We then create an `ImageGrid` object using the `ImageGrid` function and pass in the `figure`, `111` as the subplot argument, `(2, 2)` as the `nrows_ncols` argument to create a 2x2 grid of axes, and `0.1` as the `axes_pad` argument to set the padding between the axes.

```python
fig = plt.figure(figsize=(4., 4.))
grid = ImageGrid(fig, 111, nrows_ncols=(2, 2), axes_pad=0.1)
```
