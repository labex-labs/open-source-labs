# Add Lower Limits

To add lower limits to the error bars, we will use the `lolims` parameter of the `errorbar` function. We will also add a constant value of 1.0 to the y-values to differentiate this plot from the previous ones.

```python
# including lower limits
ax.errorbar(x, y + 1.0, xerr=xerr, yerr=yerr, lolims=True, linestyle='dotted')
```
