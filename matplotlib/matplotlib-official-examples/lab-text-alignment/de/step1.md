# Ein Rechteck erstellen

Wir beginnen, indem wir ein Rechteck im Diagramm mit der Funktion `Rectangle()` des Moduls `matplotlib.patches` erstellen. Nachdem das Rechteck erstellt wurde, werden wir seine horizontalen und vertikalen Grenzen mit den Funktionen `set_xlim()` und `set_ylim()` festlegen. Schließlich werden wir das Rechteck zum Diagramm hinzufügen.

```python
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots()

# Erzeuge ein Rechteck in den Achsenkoordinaten
left, width =.25,.5
bottom, height =.25,.5
right = left + width
top = bottom + height
p = Rectangle((left, bottom), width, height, fill=False)
ax.add_patch(p)

# Setze die horizontalen und vertikalen Grenzen
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.show()
```
