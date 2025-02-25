# Zweiten Teilplot erstellen

Im zweiten Teilplot werden wir `axisartist.axislines.AxesZero` verwenden, um automatisch xzero- und yzero-Achsen zu erstellen. Wir werden die anderen Spines unsichtbar machen und die xzero-Achse sichtbar setzen.

```python
ax1 = fig.add_subplot(gs[0, 1], axes_class=axisartist.axislines.AxesZero)
ax1.axis["xzero"].set_visible(True)
ax1.axis["xzero"].label.set_text("Achse Null")
ax1.axis["bottom", "top", "right"].set_visible(False)
```
