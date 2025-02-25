# Das Diagramm erstellen

Wir können jetzt das Diagramm erstellen, indem wir das `PathPatch`-Objekt zur Achse hinzufügen und einen roten Punkt plotten, der auf der Kurve liegen sollte. Wir werden auch den Titel des Diagramms auf `'Bezier Curve'` setzen.

```python
fig, ax = plt.subplots()

ax.add_patch(bezier_patch)
ax.plot([0.75], [0.25], "ro")
ax.set_title('Bezier Curve')

plt.show()
```

Der endgültige Code sollte so aussehen:

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.path as mpath

Path = mpath.Path

bezier_path = Path([(0, 0), (1, 0), (1, 1), (0, 0)],
                   [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY])

bezier_patch = mpatches.PathPatch(bezier_path, fc="none")

fig, ax = plt.subplots()

ax.add_patch(bezier_patch)
ax.plot([0.75], [0.25], "ro")
ax.set_title('Bezier Curve')

plt.show()
```
