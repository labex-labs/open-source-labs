# Create Figure and Subplot

Next, we create a figure and add a subplot with AxesZero. This creates an axis line with x and y axis labels, but no tick marks or grids.

```python
fig = plt.figure()
fig.subplots_adjust(right=0.85)
ax = fig.add_subplot(axes_class=AxesZero)
```
