# Ersten Teilplot erstellen

Im ersten Teilplot werden wir eine neue Achse erstellen, die durch y = 0 verläuft, mithilfe von `axisartist.Axes`. Wir werden auch die anderen Spines unsichtbar machen.

```python
ax0 = fig.add_subplot(gs[0, 0], axes_class=axisartist.Axes)
ax0.axis["y=0"] = ax0.new_floating_axis(nth_coord=0, value=0, axis_direction="bottom")
ax0.axis["y=0"].toggle(all=True)
ax0.axis["y=0"].label.set_text("y = 0")
ax0.axis["bottom", "top", "right"].set_visible(False)
```
