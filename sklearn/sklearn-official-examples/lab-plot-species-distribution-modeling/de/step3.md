# Karteigitter erstellen

In diesem Schritt werden wir das Karteigitter aus dem Datenobjekt erstellen. Wir werden eine Funktion namens construct_grids erstellen, die das Datenobjekt als Eingabe nimmt und das xgrid und ygrid zurückgibt.

```python
def construct_grids(batch):
    """Erstelle das Karteigitter aus dem Batch-Objekt

    Parameter
    ----------
    batch : Batch-Objekt
        Das Objekt, das von fetch_species_distributions zurückgegeben wird

    Rückgabe
    -------
    (xgrid, ygrid) : 1-D Arrays
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

# Erstelle das Karteigitter
xgrid, ygrid = construct_grids(data)
```
