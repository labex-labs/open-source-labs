# Composer une légende personnalisée

Dans cette étape, nous allons créer une légende personnalisée à l'aide d'objets Matplotlib. Tout d'abord, nous importons la classe `Line2D` du module `matplotlib.lines`. Ensuite, nous créons une liste d'objets `Line2D` avec des attributs de couleur, de largeur et d'étiquette personnalisés. Enfin, nous traçons à nouveau les données à l'aide de la fonction `plot` et appelons `legend()` avec les lignes personnalisées et les étiquettes correspondantes.

```python
# Import Line2D class
from matplotlib.lines import Line2D

# Create custom lines
custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

# Plot data and generate custom legend
fig, ax = plt.subplots()
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot'])
```
