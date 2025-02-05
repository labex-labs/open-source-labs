# Add Vertical Lines

In this step, we will add vertical lines to the plot. We will use Matplotlib's `vlines` function to draw the vertical lines. We will also use the `transform` parameter to set the y-coordinates to be scaled from 0 to 1. We will draw two vertical lines at x=1 and x=2.

```python
# Add vertical lines
vax.plot(t, s + nse, '^')
vax.vlines(t, [0], s)
vax.vlines([1, 2], 0, 1, transform=vax.get_xaxis_transform(), colors='r')
vax.set_xlabel('time (s)')
vax.set_title('Vertical lines demo')
```
