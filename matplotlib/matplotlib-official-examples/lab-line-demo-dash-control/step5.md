# Modify the dash sequence using `.Line2D.set_dashes()`

We can modify the dash sequence using `.Line2D.set_dashes()`. In this example, we modify the dash sequence for `line1` to create a dash pattern of 2pt line, 2pt break, 10pt line, and 2pt break. We also set the cap style to 'round' using `line1.set_dash_capstyle()`.

```python
line1, = ax.plot(x, y, label='Using set_dashes() and set_dash_capstyle()')
line1.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break.
line1.set_dash_capstyle('round')
```
