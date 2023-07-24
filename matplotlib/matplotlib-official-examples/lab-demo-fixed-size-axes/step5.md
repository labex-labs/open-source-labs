# Add Axes to the Figure

We will add the axes to the figure using the `add_axes()` function and passing in the position of the `Divider` object.

```python
ax = fig.add_axes(divider.get_position(),
                  axes_locator=divider.new_locator(nx=1, ny=1))
```
