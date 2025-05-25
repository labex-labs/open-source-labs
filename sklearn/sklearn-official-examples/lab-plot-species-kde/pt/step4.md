# Construir Malhas

Agora, construiremos a malha do mapa a partir do objeto de lote. Usaremos a função `construct_grids` para isso.

```python
def construct_grids(batch):
    """Construir a malha do mapa a partir do objeto de lote

    Parâmetros
    ----------
    batch : Objeto Batch
        O objeto retornado por :func:`fetch_species_distributions`

    Retorna
    -------
    (xgrid, ygrid) : arrays 1-D
        A malha correspondente aos valores em batch.coverages
    """
    # Coordenadas x,y para células de canto
    xmin = batch.x_left_lower_corner + batch.grid_size
    xmax = xmin + (batch.Nx * batch.grid_size)
    ymin = batch.y_left_lower_corner + batch.grid_size
    ymax = ymin + (batch.Ny * batch.grid_size)

    # Coordenadas x das células da malha
    xgrid = np.arange(xmin, xmax, batch.grid_size)
    # Coordenadas y das células da malha
    ygrid = np.arange(ymin, ymax, batch.grid_size)

    return (xgrid, ygrid)

# Chamar a função e armazenar os resultados em xgrid e ygrid
xgrid, ygrid = construct_grids(data)
```
