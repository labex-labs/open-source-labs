# Adjust the limits of the plot

Next, we will adjust the limits of the plot so that the diagonal line is no longer at a 45-degree angle when viewed on the screen. This will create a scenario where we need to rotate text relative to the line, rather than the screen coordinate system.

```python
# set limits so that it no longer looks on screen to be 45 degrees
ax.set_xlim([-10, 20])
```
