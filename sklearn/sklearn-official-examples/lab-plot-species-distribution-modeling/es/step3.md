# Construir la cuadrícula del mapa

En este paso, construiremos la cuadrícula del mapa a partir del objeto de datos. Crearemos una función llamada construct_grids que toma el objeto de datos como entrada y devuelve xgrid e ygrid.

```python
def construct_grids(batch):
    """Construir la cuadrícula del mapa a partir del objeto batch

    Parámetros
    ----------
    batch : Objeto Batch
        El objeto devuelto por fetch_species_distributions

    Devuelve
    -------
    (xgrid, ygrid) : arrays unidimensionales
        La cuadrícula correspondiente a los valores en batch.coverages
    """
    # Coordenadas x,y para las celdas de esquina
    xmin = batch.x_left_lower_corner + batch.grid_size
    xmax = xmin + (batch.Nx * batch.grid_size)
    ymin = batch.y_left_lower_corner + batch.grid_size
    ymax = ymin + (batch.Ny * batch.grid_size)

    # Coordenadas x de las celdas de la cuadrícula
    xgrid = np.arange(xmin, xmax, batch.grid_size)
    # Coordenadas y de las celdas de la cuadrícula
    ygrid = np.arange(ymin, ymax, batch.grid_size)

    return (xgrid, ygrid)

# Construir la cuadrícula del mapa
xgrid, ygrid = construct_grids(data)
```
