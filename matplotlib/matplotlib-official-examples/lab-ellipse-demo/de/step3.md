# Zeichnen von Ellipsen mit verschiedenen Winkeln

In diesem Beispiel werden wir viele Ellipsen mit verschiedenen Winkeln zeichnen. Wir werden eine Schleife verwenden, um für jeden Winkel, den wir zeichnen möchten, eine `Ellipse`-Instanz zu erstellen.

```python
# Definieren des Winkel-Schritts und des Winkelbereichs zum Zeichnen
angle_step = 45  # Grad
angles = np.arange(0, 180, angle_step)

# Erstellen des Plots und Festlegen des Seitenverhältnisses auf 'equal'
fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

# Schleife über die Winkel und Zeichnen einer Ellipse für jeden Winkel
for angle in angles:
    ellipse = Ellipse((0, 0), 4, 2, angle=angle, alpha=0.1)
    ax.add_artist(ellipse)

# Festlegen der x- und y-Grenzen des Plots
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)

# Anzeigen des Plots
plt.show()
```
