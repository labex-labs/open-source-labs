# Transform Coordinates

The next step is to transform the coordinates of the data and the display. We will use the `ax.transData` method to transform the data coordinates and the `figure pixels` coordinate system to transform the display coordinates.

```python
xdata, ydata = 5, 0
xdisplay, ydisplay = ax.transData.transform((xdata, ydata))
```
