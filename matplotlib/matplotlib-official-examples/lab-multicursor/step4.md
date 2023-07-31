# Adding MultiCursor

Finally, we will add the `MultiCursor` function to display a cursor on all three plots when hovering over a data point.

```python
multi = MultiCursor(None, (ax1, ax2, ax3), color='r', lw=1)
plt.show()
```
