# Construire la grille de la carte

Dans cette étape, nous allons construire la grille de la carte à partir de l'objet de données. Nous allons créer une fonction appelée construct_grids qui prend l'objet de données en entrée et renvoie xgrid et ygrid.

```python
def construct_grids(batch):
    """Construire la grille de la carte à partir de l'objet batch

    Paramètres
    ----------
    batch : Objet Batch
        L'objet renvoyé par fetch_species_distributions

    Retours
    -------
    (xgrid, ygrid) : Tableaux 1-D
        La grille correspondant aux valeurs dans batch.coverages
    """
    # Coordonnées x,y pour les cellules du coin
    xmin = batch.x_left_lower_corner + batch.grid_size
    xmax = xmin + (batch.Nx * batch.grid_size)
    ymin = batch.y_left_lower_corner + batch.grid_size
    ymax = ymin + (batch.Ny * batch.grid_size)

    # Coordonnées x des cellules de la grille
    xgrid = np.arange(xmin, xmax, batch.grid_size)
    # Coordonnées y des cellules de la grille
    ygrid = np.arange(ymin, ymax, batch.grid_size)

    return (xgrid, ygrid)

# Construire la grille de la carte
xgrid, ygrid = construct_grids(data)
```
