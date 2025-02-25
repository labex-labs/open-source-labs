# Créez une figure et un objet ImageGrid

Ensuite, nous créons un objet `figure` à l'aide de la fonction `plt.figure` et passons l'argument `figsize` pour définir la taille de la figure. Nous créons ensuite un objet `ImageGrid` à l'aide de la fonction `ImageGrid` et passons le `figure`, `111` comme argument pour le sous-graphique, `(2, 2)` comme argument `nrows_ncols` pour créer une grille 2x2 d'axes et `0.1` comme argument `axes_pad` pour définir l'espacement entre les axes.

```python
fig = plt.figure(figsize=(4., 4.))
grid = ImageGrid(fig, 111, nrows_ncols=(2, 2), axes_pad=0.1)
```
