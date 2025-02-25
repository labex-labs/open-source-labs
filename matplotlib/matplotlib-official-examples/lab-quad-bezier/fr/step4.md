# Création du tracé

Nous pouvons maintenant créer le tracé en ajoutant l'objet `PathPatch` aux axes et en traçant un point rouge qui devrait se trouver sur la courbe. Nous définirons également le titre du tracé sur `'Courbe de Bézier'`.

```python
fig, ax = plt.subplots()

ax.add_patch(bezier_patch)
ax.plot([0.75], [0.25], "ro")
ax.set_title('Courbe de Bézier')

plt.show()
```

Le code final devrait ressembler à ceci :

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
ax.set_title('Courbe de Bézier')

plt.show()
```
