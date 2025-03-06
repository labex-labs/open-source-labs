# Positionnement vertical personnalisé des titres

Parfois, vous pourriez vouloir ajuster la position verticale de votre titre. Dans cette étape, vous apprendrez à contrôler manuellement la position verticale (axe des y) des titres de vos graphiques.

## Comprendre la position en y des titres

La position verticale d'un titre peut être ajustée en utilisant le paramètre `y` dans la fonction `title()`. Le paramètre `y` accepte des valeurs en coordonnées normalisées, où :

- `y = 1.0` (par défaut) place le titre en haut du graphique
- `y > 1.0` place le titre au - dessus du haut du graphique
- `y < 1.0` place le titre en dessous du haut du graphique, le rapprochant du contenu du graphique

## Création d'un graphique avec une position en y personnalisée pour le titre

Créons un graphique avec le titre positionné plus haut que la position par défaut. Dans une nouvelle cellule, entrez le code suivant :

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Higher Title Position', y=1.1)  # Position the title higher
plt.show()
```

Exécutez la cellule. Remarquez comment le titre apparaît maintenant légèrement plus haut au - dessus du graphique par rapport à la position par défaut.

Maintenant, créons un graphique avec le titre positionné plus bas que la position par défaut :

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Lower Title Position', y=0.9)  # Position the title lower
plt.show()
```

Exécutez la cellule. Le titre devrait maintenant apparaître plus proche du contenu du graphique.

## Comparaison de différentes positions en y

Créons plusieurs graphiques côte à côte pour comparer différentes positions verticales de titre :

```python
# Create a figure with 3 subplots arranged horizontally
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Plot 1: Default Y-position
axes[0].plot(range(10))
axes[0].grid(True)
axes[0].set_title('Default Position (y=1.0)')

# Plot 2: Higher Y-position
axes[1].plot(range(10))
axes[1].grid(True)
axes[1].set_title('Higher Position', y=1.15)

# Plot 3: Lower Y-position
axes[2].plot(range(10))
axes[2].grid(True)
axes[2].set_title('Lower Position', y=0.85)

plt.tight_layout()  # Adjust spacing between subplots
plt.show()
```

Exécutez la cellule pour voir les trois positions verticales côte à côte. Cette comparaison vous aide à comprendre comment le paramètre `y` affecte la position verticale du titre.

## Combinaison du positionnement horizontal et vertical

Vous pouvez combiner le paramètre `loc` (pour l'alignement horizontal) avec le paramètre `y` (pour la position verticale) pour placer votre titre exactement là où vous le voulez :

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Custom Positioned Title', loc='right', y=1.1)  # Right-aligned and higher
plt.show()
```

Exécutez la cellule. Le titre devrait maintenant apparaître aligné avec le bord droit du graphique et positionné plus haut que la position par défaut.
