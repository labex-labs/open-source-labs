# Construir la malla

Ahora construiremos la malla del mapa a partir del objeto de lote. Utilizaremos la función `construct_grids` para lograr esto.

```python
def construct_grids(batch):
    """Construir la malla del mapa a partir del objeto de lote

    Parámetros
    ----------
    batch : Objeto de lote
        El objeto devuelto por :func:`fetch_species_distributions`

    Devuelve
    -------
    (xgrid, ygrid) : Arrays unidimensionales
        La malla correspondiente a los valores en batch.coverages
    """
    # Coordenadas x,y para las celdas de esquina
    xmin = batch.x_left_lower_corner + batch.grid_size
    xmax = xmin + (batch.Nx * batch.grid_size)
    ymin = batch.y_left_lower_corner + batch.grid_size
    ymax = ymin + (batch.Ny * batch.grid_size)

    # Coordenadas x de las celdas de la malla
    xgrid = np.arange(xmin, xmax, batch.grid_size)
    # Coordenadas y de las celdas de la malla
    ygrid = np.arange(ymin, ymax, batch.grid_size)

    return (xgrid, ygrid)

# Llame a la función y almacene los resultados en xgrid e ygrid
xgrid, ygrid = construct_grids(data)
```
