# Move the x-axis tick labels to the top

To move the x-axis tick labels to the top, we will use the `tick_params()` function and set the `top` and `labeltop` parameters to `True`, and the `bottom` and `labelbottom` parameters to `False`.

```python
ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
```
