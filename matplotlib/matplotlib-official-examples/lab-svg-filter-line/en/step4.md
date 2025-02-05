# Draw Shadows

We draw shadows for the lines by using the same lines with a slight offset and gray colors. We adjust the color and zorder of the shadow lines so that they are drawn below the original lines. We also use the `offset_copy()` method to create an offset transform for the shadow lines.

```python
for l in [l1, l2]:
    xx = l.get_xdata()
    yy = l.get_ydata()
    shadow, = ax.plot(xx, yy)
    shadow.update_from(l)

    shadow.set_color("0.2")
    shadow.set_zorder(l.get_zorder() - 0.5)

    transform = mtransforms.offset_copy(l.get_transform(), fig1, x=4.0, y=-6.0, units='points')
    shadow.set_transform(transform)

    shadow.set_gid(l.get_label() + "_shadow")
```
