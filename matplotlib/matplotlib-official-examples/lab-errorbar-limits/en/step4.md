# Add Upper Limits

To add upper limits to the error bars, we will use the `uplims` parameter of the `errorbar` function. We will also add a constant value of 0.5 to the y-values to differentiate this plot from the previous one.

```python
# including upper limits
ax.errorbar(x, y + 0.5, xerr=xerr, yerr=yerr, uplims=True, linestyle='dotted')
```
