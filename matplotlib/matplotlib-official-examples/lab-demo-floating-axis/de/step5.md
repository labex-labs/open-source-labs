# Erstellen von schwebenden Achsen

In diesem Schritt werden wir zwei schwebende Achsen erstellen, die zur Darstellung der Polarkurve in einem rechteckigen Rahmen verwendet werden sollen. Wir werden `new_floating_axis()` verwenden, um die schwebenden Achsen zu erstellen.

```python
# Erstellen der schwebenden Achsen
ax1.axis["lat"] = axis = ax1.new_floating_axis(0, 60)
axis.label.set_text(r"$\theta = 60^{\circ}$")
axis.label.set_visible(True)

ax1.axis["lon"] = axis = ax1.new_floating_axis(1, 6)
axis.label.set_text(r"$r = 6$")
```
