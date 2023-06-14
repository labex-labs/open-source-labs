# Create the Figure and Axes

We need to create the figure and axes for the barcode. We will set the figure size to a multiple of the number of data points, and turn off all axis.

```python
fig = plt.figure(figsize=(len(code) * pixel_per_bar / dpi, 2), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])  # span the whole figure
ax.set_axis_off()
```

#
