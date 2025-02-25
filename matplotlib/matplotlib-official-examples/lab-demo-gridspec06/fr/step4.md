# Création des grilles intérieures et des sous-graphiques

Dans cette étape, nous allons créer les grilles intérieures et les sous-graphiques en utilisant des `.GridSpec` imbriqués. Nous allons parcourir chaque cellule de la grille extérieure et créer une grille 3x3 pour chaque cellule.

```python
for a in range(4):
    for b in range(4):
        # gridspec à l'intérieur d'un gridspec
        inner_grid = outer_grid[a, b].subgridspec(3, 3, wspace=0, hspace=0)
        axs = inner_grid.subplots()  # Crée tous les sous-graphiques pour la grille intérieure.
        for (c, d), ax in np.ndenumerate(axs):
            ax.plot(*squiggle_xy(a + 1, b + 1, c + 1, d + 1))
            ax.set(xticks=[], yticks=[])
```
