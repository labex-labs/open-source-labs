# Add Horizontal Lines

In this step, we will add horizontal lines to the plot. We will use Matplotlib's `hlines` function to draw the horizontal lines. We will draw horizontal lines at y=0.5, y=2.5, and y=4.5.

```python
# Add horizontal lines
hax.plot(s + nse, t, '^')
hax.hlines(t, [0], s, lw=2)
hax.set_xlabel('time (s)')
hax.set_title('Horizontal lines demo')
```
