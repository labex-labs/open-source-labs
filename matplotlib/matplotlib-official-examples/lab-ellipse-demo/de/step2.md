# Zeichnen einzelner Ellipsen

In diesem Beispiel werden wir viele Ellipsen mit zufälligen Größen, Positionen und Farben zeichnen. Jede Ellipse wird eine Instanz der `Ellipse`-Klasse sein.

```python
# Fixieren des Zufallszustands für Reproduzierbarkeit
np.random.seed(19680801)

# Anzahl der zu zeichnenden Ellipsen
NUM = 250

# Generieren der Ellipsen
ells = [Ellipse(xy=np.random.rand(2) * 10,
                width=np.random.rand(), height=np.random.rand(),
                angle=np.random.rand() * 360)
        for i in range(NUM)]

# Erstellen des Plots und Festlegen des Seitenverhältnisses auf 'equal'
fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

# Hinzufügen jeder Ellipse zum Plot
for e in ells:
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
    e.set_alpha(np.random.rand())
    e.set_facecolor(np.random.rand(3))

# Festlegen der x- und y-Grenzen des Plots
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Anzeigen des Plots
plt.show()
```
