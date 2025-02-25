# Zweite y-Achse erstellen

Schließlich werden wir eine neue y2-Achse auf der rechten Seite des Diagramms mit einem Offset von (20, 0) erstellen und sie beschriften.

```python
ax.axis["right2"] = ax.new_fixed_axis(loc="right", offset=(20, 0))
ax.axis["right2"].label.set_text("Label Y2")
```
