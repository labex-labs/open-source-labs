# Achsenbeschriftungen festlegen

Wir legen die Achsenbeschriftungen für die linke und rechte Seite des Diagramms mit der Funktion `ax1.axis[]` fest. Wir legen auch die Richtung der Strichmarkenbeschriftungen mit der Funktion `set_axis_direction()` fest.

```python
ax1.axis["left"].major_ticklabels.set_axis_direction("top")
ax1.axis["left"].label.set_text("Left label")

ax1.axis["right"].label.set_visible(True)
ax1.axis["right"].label.set_text("Right label")
ax1.axis["right"].label.set_axis_direction("left")
```
