# Filling the Box Plots with Custom Colors

Next, we will fill the box plots with custom colors. We will create a list of colors and use a loop to fill each box with a different color.

```python
colors = ['pink', 'lightblue', 'lightgreen']
for bplot in (bplot1, bplot2):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)
```
