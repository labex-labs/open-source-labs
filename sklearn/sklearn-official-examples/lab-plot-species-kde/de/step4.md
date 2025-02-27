# Gitter erstellen

Wir werden nun das Kartengitter aus dem Batch-Objekt erstellen. Dazu verwenden wir die Funktion `construct_grids`.

```python
def construct_grids(batch):
    """Construct the map grid from the batch object

    Parameters
    ----------
    batch : Batch object
        Das von :func:`fetch_species_distributions` zurückgegebene Objekt

    Returns
    -------
    (xgrid, ygrid) : 1-D arrays
        Das Gitter, das den Werten in batch.coverages entspricht
    """
    # x,y-Koordinaten für die Eckzellen
    xmin = batch.x_left_lower_corner + batch.grid_size
    xmax = xmin + (batch.Nx * batch.grid_size)
    ymin = batch.y_left_lower_corner + batch.grid_size
    ymax = ymin + (batch.Ny * batch.grid_size)

    # x-Koordinaten der Gitterzellen
    xgrid = np.arange(xmin, xmax, batch.grid_size)
    # y-Koordinaten der Gitterzellen
    ygrid = np.arange(ymin, ymax, batch.grid_size)

    return (xgrid, ygrid)

# Rufen Sie die Funktion auf und speichern Sie die Ergebnisse in xgrid und ygrid
xgrid, ygrid = construct_grids(data)
```
