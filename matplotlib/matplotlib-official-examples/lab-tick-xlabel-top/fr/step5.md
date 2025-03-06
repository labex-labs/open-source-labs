# Enregistrer et partager votre graphique

La dernière étape consiste à enregistrer votre graphique personnalisé afin de le inclure dans des rapports, des présentations ou de le partager avec d'autres personnes.

## Enregistrer des graphiques dans différents formats

Matplotlib vous permet d'enregistrer des graphiques dans divers formats, notamment PNG, JPG, PDF, SVG, etc. Apprenons à enregistrer notre graphique dans différents formats :

```python
# Create a plot similar to our previous customized one
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot the data
ax.plot(x, y1, linewidth=2, color='blue', label='sin(x)')
ax.plot(x, y2, linewidth=2, color='red', label='cos(x)')

# Move the x-axis tick labels to the top
ax.tick_params(
    axis='x',
    top=True,
    labeltop=True,
    bottom=False,
    labelbottom=False
)

# Customize tick labels
ax.set_xticks(np.arange(0, 2*np.pi + 0.1, np.pi/2))
ax.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])

# Add title and labels
ax.set_title('Plot with X-Axis Labels at the Top', fontsize=14)
ax.set_xlabel('X-axis at the top')
ax.set_ylabel('Y-axis')

# Add grid and legend
ax.grid(True)
ax.legend()

# Save the figure in different formats
plt.savefig('plot_with_top_xlabels.png', dpi=300, bbox_inches='tight')
plt.savefig('plot_with_top_xlabels.pdf', bbox_inches='tight')
plt.savefig('plot_with_top_xlabels.svg', bbox_inches='tight')

# Show the plot
plt.show()

print("The plot has been saved in PNG, PDF, and SVG formats in the current directory.")
```

Lorsque vous exécutez ce code, le graphique sera enregistré dans trois formats différents :

- PNG : Un format d'image raster adapté pour le web et l'utilisation générale
- PDF : Un format vectoriel idéal pour les publications et les rapports
- SVG : Un format vectoriel excellent pour le web et les graphiques éditables

Les fichiers seront enregistrés dans le répertoire de travail actuel de votre notebook Jupyter.

## Comprendre les paramètres d'enregistrement

Examinons les paramètres utilisés avec `savefig()` :

- `dpi=300` : Définit la résolution (points par pouce) pour les formats raster comme le PNG
- `bbox_inches='tight'` : Ajuste automatiquement les limites de la figure pour inclure tous les éléments sans espace blanc inutile

## Visualiser les fichiers enregistrés

Vous pouvez visualiser les fichiers enregistrés en accédant au navigateur de fichiers de Jupyter :

1. Cliquez sur le logo "Jupyter" en haut à gauche
2. Dans le navigateur de fichiers, vous devriez voir les fichiers d'image enregistrés
3. Cliquez sur n'importe quel fichier pour le visualiser ou le télécharger

## Options d'exportation supplémentaires pour les graphiques

Pour avoir plus de contrôle sur le graphique enregistré, vous pouvez personnaliser la taille de la figure, ajuster le fond ou modifier la résolution (DPI) selon vos besoins :

```python
# Control the background color and transparency
fig.patch.set_facecolor('white')  # Set figure background color
fig.patch.set_alpha(0.8)          # Set background transparency

# Save with custom settings
plt.savefig('custom_background_plot.png',
            dpi=400,              # Higher resolution
            facecolor=fig.get_facecolor(),  # Use the figure's background color
            edgecolor='none',     # No edge color
            bbox_inches='tight',  # Tight layout
            pad_inches=0.1)       # Add a small padding

print("A customized plot has been saved with specialized export settings.")
```

Cela montre comment enregistrer des graphiques avec un contrôle précis sur le format de sortie et l'apparence.
