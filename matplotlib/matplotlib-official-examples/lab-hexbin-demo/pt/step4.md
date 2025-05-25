# Adicionar uma Escala de Cores Logarítmica

Podemos adicionar uma escala de cores logarítmica ao gráfico de binning hexagonal definindo `bins='log'` em `hexbin()`.

```python
fig, ax = plt.subplots(figsize=(9, 4))

hb = ax.hexbin(x, y, gridsize=50, bins='log', cmap='inferno')
ax.set(xlim=xlim, ylim=ylim)
ax.set_title("With a log color scale")

cb = fig.colorbar(hb, ax=ax, label='log10(N)')
```
