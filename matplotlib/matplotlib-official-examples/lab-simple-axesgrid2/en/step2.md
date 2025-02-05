# Create a Figure and ImageGrid

Next, we create a figure and ImageGrid with `nrows_ncols` parameter to define the number of rows and columns of the grid.

```python
fig = plt.figure(figsize=(5.5, 3.5))
grid = ImageGrid(fig, 111,  # similar to subplot(111)
                 nrows_ncols=(1, 3),
                 axes_pad=0.1,
                 label_mode="L")
```
