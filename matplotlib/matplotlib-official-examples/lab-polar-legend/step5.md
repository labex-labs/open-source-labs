# Customize Plot

We can customize our plot by changing the grid color and adding a legend. In this example, we will move the legend slightly away from the center of the plot to avoid overlap.

```python
ax.tick_params(grid_color="palegoldenrod")
angle = np.deg2rad(67.5)
ax.legend(loc="lower left",
          bbox_to_anchor=(.5 + np.cos(angle)/2, .5 + np.sin(angle)/2))
```
