# Créer un graphique de base avec les paramètres par défaut

Maintenant que nous avons importé Matplotlib, créons un graphique simple avec les paramètres par défaut pour comprendre comment les axes et les étiquettes de graduation sont positionnés par défaut.

## Comprendre les composants de Matplotlib

Dans Matplotlib, les graphiques sont composés de plusieurs éléments :

- **Figure** : Le conteneur global du graphique
- **Axes** : La zone où les données sont tracées avec son propre système de coordonnées
- **Axis** : Les objets ressemblant à des axes de nombres qui définissent le système de coordonnées
- **Ticks** : Les marques sur les axes qui indiquent des valeurs spécifiques
- **Tick Labels** : Les étiquettes de texte qui indiquent la valeur de chaque graduation

Par défaut, les étiquettes de graduation de l'axe des x apparaissent en bas du graphique.

## Créer un graphique simple

Dans une nouvelle cellule de votre notebook, créons un simple graphique linéaire :

```python
# Create a figure and a set of axes
fig, ax = plt.subplots(figsize=(8, 5))

# Generate some data
x = np.arange(0, 10, 1)
y = np.sin(x)

# Plot the data
ax.plot(x, y, marker='o', linestyle='-', color='blue', label='sin(x)')

# Add a title and labels
ax.set_title('A Simple Sine Wave Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis (sin(x))')

# Add a grid and legend
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()

# Display the plot
plt.show()

print("Notice that the x-axis tick labels are at the bottom of the plot by default.")
```

Lorsque vous exécutez ce code, vous verrez un graphique d'onde sinusoïdale avec les étiquettes de graduation de l'axe des x en bas du graphique, qui est la position par défaut dans Matplotlib.

Prenez un moment pour observer la structure du graphique et la position des étiquettes de graduation. Cette compréhension nous aidera à apprécier les modifications que nous allons apporter à l'étape suivante.
