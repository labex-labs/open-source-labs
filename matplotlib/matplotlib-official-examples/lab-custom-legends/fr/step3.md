# Composer une légende personnalisée avec différents objets Matplotlib

Dans cette étape, nous allons créer une légende personnalisée à l'aide de différents objets Matplotlib, y compris `Line2D` et `Patch`. Tout d'abord, nous importons la classe `Patch` du module `matplotlib.patches`. Ensuite, nous créons une liste d'objets `Line2D` et `Patch` avec des attributs personnalisés. Enfin, nous appelons `legend()` avec les objets personnalisés et les étiquettes correspondantes.

```python
# Import Line2D and Patch classes
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

# Create legend elements
legend_elements = [Line2D([0], [0], color='b', lw=4, label='Ligne'),
                   Line2D([0], [0], marker='o', color='w', label='Nuage de points',
                          markerfacecolor='g', markersize=15),
                   Patch(facecolor='orange', edgecolor='r',
                         label='Patch de couleur')]

# Plot data and generate custom legend
fig, ax = plt.subplots()
ax.legend(handles=legend_elements, loc='center')
```
