# Create a simple arrow

Now, we will create a simple anchored direction arrow using the AnchoredDirectionArrows class. This arrow will indicate the X and Y directions in the plot.

```python
# Simple example
simple_arrow = AnchoredDirectionArrows(ax.transAxes, 'X', 'Y')
ax.add_artist(simple_arrow)
```
