# Criar Dados

Nesta etapa, criaremos alguns dados para visualizar. Criaremos um gráfico de dispersão (scatter plot) de pontos em uma grade.

```python
fig, ax = plt.subplots()
grid_size = 5
grid_x = np.tile(np.arange(grid_size), grid_size)
grid_y = np.repeat(np.arange(grid_size), grid_size)
pts = ax.scatter(grid_x, grid_y)
```
