# Positionnement avancé des titres avec des sous - graphiques

Dans cette étape, vous apprendrez des techniques avancées de positionnement des titres lorsque vous travaillez avec des mises en page de sous - graphiques et des objets d'axe. Vous apprendrez également à utiliser la fonction `suptitle()` pour ajouter un titre global à une figure avec plusieurs sous - graphiques.

## Création d'une figure avec des sous - graphiques et des titres individuels

Créons une grille de sous - graphiques 2x2, chacun avec son propre titre positionné différemment :

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Flatten the 2D array of axes for easier iteration
axes = axes.flatten()

# Plot data and set titles with different positions for each subplot
for i, ax in enumerate(axes):
    ax.plot(range(10))
    ax.grid(True)

# Top-left subplot: Default centered title
axes[0].set_title('Default (Centered)')

# Top-right subplot: Left-aligned title
axes[1].set_title('Left-Aligned', loc='left')

# Bottom-left subplot: Right-aligned title
axes[2].set_title('Right-Aligned', loc='right')

# Bottom-right subplot: Custom positioned title
axes[3].set_title('Custom Position', y=0.85, loc='center')

# Add spacing between subplots
plt.tight_layout()
plt.show()
```

Exécutez la cellule. Vous devriez voir quatre sous - graphiques, chacun avec un titre positionné différemment.

## Ajout d'un titre au niveau de la figure avec suptitle()

Lorsque vous travaillez avec plusieurs sous - graphiques, vous pourriez vouloir ajouter un titre global pour l'ensemble de la figure. Cela peut être fait en utilisant la fonction `suptitle()` :

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Flatten the 2D array of axes for easier iteration
axes = axes.flatten()

# Plot data on each subplot
for i, ax in enumerate(axes):
    ax.plot(range(10))
    ax.grid(True)
    ax.set_title(f'Subplot {i+1}')

# Add an overall title to the figure
fig.suptitle('Multiple Subplots with an Overall Title', fontsize=16)

# Add spacing between subplots
plt.tight_layout()
# Add top spacing for the suptitle
plt.subplots_adjust(top=0.9)
plt.show()
```

Exécutez la cellule. Vous devriez voir quatre sous - graphiques, chacun avec son propre titre, et un titre global pour la figure en haut.

## Combinaison de titres d'axes et de titres de figure

Vous pouvez combiner des titres de sous - graphiques individuels avec un titre global de figure :

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Plot data on each subplot with different title positions
axes[0, 0].plot(range(10))
axes[0, 0].grid(True)
axes[0, 0].set_title('Centered Title', loc='center')

axes[0, 1].plot(range(10))
axes[0, 1].grid(True)
axes[0, 1].set_title('Left-Aligned Title', loc='left')

axes[1, 0].plot(range(10))
axes[1, 0].grid(True)
axes[1, 0].set_title('Right-Aligned Title', loc='right')

axes[1, 1].plot(range(10))
axes[1, 1].grid(True)
axes[1, 1].set_title('Lower Title', y=0.85)

# Add an overall title to the figure
fig.suptitle('Advanced Title Positioning Demo', fontsize=16)

# Add spacing between subplots
plt.tight_layout()
# Add top spacing for the suptitle
plt.subplots_adjust(top=0.9)
plt.show()
```

Exécutez la cellule. Vous devriez voir une figure avec quatre sous - graphiques, chacun avec un titre positionné différemment, et un titre global en haut de la figure.

La fonction `suptitle()` est utile pour ajouter un titre principal qui décrit l'ensemble de la figure, tandis que les appels individuels de `set_title()` sur les objets d'axe ajoutent des titres plus spécifiques à chaque sous - graphique.
