# Construir Grade do Mapa

Neste passo, construiremos a grade do mapa a partir do objeto de dados. Criaremos uma função chamada `construct_grids` que recebe o objeto de dados como entrada e retorna as grades `xgrid` e `ygrid`.

```python
def construct_grids(batch):
    """Construir a grade do mapa a partir do objeto batch

    Parâmetros
    ----------
    batch : Objeto Batch
        O objeto retornado por fetch_species_distributions

    Retorna
    -------
    (xgrid, ygrid) : arrays 1-D
        A grade correspondente aos valores em batch.coverages
    """
    # Coordenadas x,y para as células de canto
    xmin = batch.x_left_lower_corner + batch.grid_size
    xmax = xmin + (batch.Nx * batch.grid_size)
    ymin = batch.y_left_lower_corner + batch.grid_size
    ymax = ymin + (batch.Ny * batch.grid_size)

    # Coordenadas x das células da grade
    xgrid = np.arange(xmin, xmax, batch.grid_size)
    # Coordenadas y das células da grade
    ygrid = np.arange(ymin, ymax, batch.grid_size)

    return (xgrid, ygrid)

# Construir a grade do mapa
xgrid, ygrid = construct_grids(data)
```
