# Set other attributes of the dash using relevant methods

Other attributes of the dash may also be set using relevant methods like `~.Line2D.set_dash_joinstyle()`, `~.Line2D.set_dash_joinstyle()`, and `~.Line2D.set_gapcolor()`. In this example, we will be using the `dashes` and `gapcolor` parameters to set the dash sequence and alternating color for `line3`.

```python
line3, = ax.plot(x, y - 0.4, dashes=[4, 4], gapcolor='tab:pink',
                 label='Using the dashes and gapcolor parameters')
```
