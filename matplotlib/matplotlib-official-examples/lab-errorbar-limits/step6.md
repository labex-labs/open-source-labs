# Add Upper and Lower Limits

To add both upper and lower limits to the error bars, we will use both the `uplims` and `lolims` parameters of the `errorbar` function. We will also add a marker to the plot to differentiate it from the previous ones.

```python
# including upper and lower limits
ax.errorbar(x, y + 1.5, xerr=xerr, yerr=yerr, lolims=True, uplims=True,
            marker='o', markersize=8, linestyle='dotted')
```
