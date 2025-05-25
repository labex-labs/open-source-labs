# Criar o Gráfico de Binning Hexagonal

Criaremos o gráfico de binning hexagonal usando `matplotlib.pyplot.hexbin()`.

```python
fig, ax = plt.subplots(figsize=(9, 4))

hb = ax.hexbin(x, y, gridsize=50, cmap='inferno')
ax.set(xlim=xlim, ylim=ylim)
ax.set_title("Hexagon binning")

cb = fig.colorbar(hb, ax=ax, label='counts')
```

Aqui, definimos o tamanho da grade (grid size) para 50 e o mapa de cores (color map) para 'inferno'. Também adicionamos uma barra de cores para mostrar a contagem de pontos de dados dentro de cada hexágono.
