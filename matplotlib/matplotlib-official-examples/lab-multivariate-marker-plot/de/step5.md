# Diagramm erstellen

In diesem Schritt erstellst du das Diagramm mit den zuvor generierten zufälligen Daten. Insbesondere zeichnest du jeden Datenpunkt als Marker mit dem Erfolgssymbol, das durch die Variable "erfolg" bestimmt wird, der Größe, die durch die Variable "fähigkeit" bestimmt wird, der Rotation, die durch die Variable "Abflugwinkel" bestimmt wird, und der Farbe, die durch die Variable "Kraft" bestimmt wird.

```python
fig, ax = plt.subplots()
fig.suptitle("Throwing success", size=14)
for skill, takeoff, thrust, mood, pos in data:
    t = Affine2D().scale(skill).rotate_deg(takeoff)
    m = MarkerStyle(SUCCESS_SYMBOLS[mood], transform=t)
    ax.plot(pos[0], pos[1], marker=m, color=cmap(thrust))
fig.colorbar(plt.cm.ScalarMappable(norm=Normalize(0, 1), cmap=cmap),
             ax=ax, label="Normalized Thrust [a.u.]")
ax.set_xlabel("X position [m]")
ax.set_ylabel("Y position [m]")
```
