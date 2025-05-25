# Criar as Grelhas Internas e Subplots

Nesta etapa, criaremos as grelhas internas e subplots usando `.GridSpec`s aninhados. Iremos iterar por cada célula na grelha externa e criar uma grelha 3x3 para cada célula.

```python
for a in range(4):
    for b in range(4):
        # gridspec inside gridspec
        inner_grid = outer_grid[a, b].subgridspec(3, 3, wspace=0, hspace=0)
        axs = inner_grid.subplots()  # Create all subplots for the inner grid.
        for (c, d), ax in np.ndenumerate(axs):
            ax.plot(*squiggle_xy(a + 1, b + 1, c + 1, d + 1))
            ax.set(xticks=[], yticks=[])
```
