# Diagramm anpassen

Wir können unser Diagramm anpassen, indem wir die Gitterfarbe ändern und eine Legende hinzufügen. In diesem Beispiel werden wir die Legende leicht vom Zentrum des Diagramms weg bewegen, um Überlappungen zu vermeiden.

```python
ax.tick_params(grid_color="palegoldenrod")
angle = np.deg2rad(67.5)
ax.legend(loc="lower left",
          bbox_to_anchor=(.5 + np.cos(angle)/2,.5 + np.sin(angle)/2))
```
