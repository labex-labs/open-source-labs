# Set the position of the colorbar label

We can set the position of the colorbar label using the `colorbar` method and the `set_label` method. We can set the position to `'top'`, `'bottom'`, `'left'`, or `'right'`. In this example, we will set the position to `'top'`.

```python
cbar = fig.colorbar(sc)
cbar.set_label("ZLabel", loc='top')
```
