# Remove the Major Tick Labels and Minor Ticks

To fake the behavior of centering the labels between ticks, we need to remove the major tick labels and minor ticks and only show the minor tick labels. We can do this using the `tick_params()` function and setting the `tick1On` and `tick2On` parameters to `False`.

```python
# Remove the tick lines
ax.tick_params(axis='x', which='minor', tick1On=False, tick2On=False)
```
