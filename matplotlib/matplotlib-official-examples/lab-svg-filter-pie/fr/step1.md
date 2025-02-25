# Créer un diagramme circulaire

Nous allons créer une figure carrée et des axes pour notre diagramme circulaire. Nous allons définir les étiquettes et les fracs pour le graphique. Nous allons également définir les valeurs d'explosion pour les tranches du diagramme. Enfin, nous allons tracer le diagramme circulaire avec les paramètres définis.

```python
import matplotlib.pyplot as plt
from matplotlib.patches import Shadow

fig = plt.figure(figsize=(6, 6))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
fracs = [15, 30, 45, 10]
explode = (0, 0.05, 0, 0)

pies = ax.pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%')

for w in pies[0]:
    w.set_gid(w.get_label())
    w.set_edgecolor("none")

for w in pies[0]:
    s = Shadow(w, -0.01, -0.01)
    s.set_gid(w.get_gid() + "_shadow")
    s.set_zorder(w.get_zorder() - 0.1)
    ax.add_patch(s)

plt.show()
```
