# Setting JoinStyle

We can set the `JoinStyle` of the line using the `set_solid_joinstyle()` method of the `Line2D` object. We will create a new line object and set its join style to `JoinStyle.bevel`.

```python
line = ax.lines[0]
line.set_solid_joinstyle(JoinStyle.bevel)
```
