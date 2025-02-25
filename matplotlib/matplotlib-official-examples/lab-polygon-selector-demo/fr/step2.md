# Création de données

Dans cette étape, nous allons créer quelques données à visualiser. Nous allons créer un nuage de points sur une grille.

```python
fig, ax = plt.subplots()
grid_size = 5
grid_x = np.tile(np.arange(grid_size), grid_size)
grid_y = np.repeat(np.arange(grid_size), grid_size)
pts = ax.scatter(grid_x, grid_y)
```
