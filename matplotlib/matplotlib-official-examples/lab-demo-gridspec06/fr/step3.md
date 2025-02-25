# Création de la figure et de la grille extérieure

Ensuite, nous allons créer la figure et la grille extérieure en utilisant la fonction `add_gridspec`. Nous allons créer une grille 4x4 sans espacement entre les sous-graphiques.

```python
fig = plt.figure(figsize=(8, 8))
outer_grid = fig.add_gridspec(4, 4, wspace=0, hspace=0)
```
