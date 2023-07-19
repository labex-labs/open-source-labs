# Updating the data

We will define a method `update` that will update the data. The method will take the ax (axis) as an input parameter. We will update the line by getting the view limit and checking if the width of the view limit is different from delta. If the width of the view limit is different from delta, we will update the delta and get the xstart and xend. We will then set the data to the downsampled data and draw the idle.

```python
def update(self, ax):
    # Update the line
    lims = ax.viewLim
    if abs(lims.width - self.delta) > 1e-8:
        self.delta = lims.width
        xstart, xend = lims.intervalx
        self.line.set_data(*self.downsample(xstart, xend))
        ax.figure.canvas.draw_idle()
```
