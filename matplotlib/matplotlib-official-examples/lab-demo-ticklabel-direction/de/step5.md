# Angepasste Richtung der Skalenbeschriftungen

In diesem Schritt werden wir einen Teilplot erstellen, bei dem die Richtung der Skalenbeschriftungen angepasst ist.

```python
ax = setup_axes(fig, 132)
ax.axis["left"].set_axis_direction("right")
ax.axis["bottom"].set_axis_direction("top")
ax.axis["right"].set_axis_direction("left")
ax.axis["top"].set_axis_direction("bottom")
```
