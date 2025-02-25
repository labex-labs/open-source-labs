# Agregar una escala de color logarítmica

Podemos agregar una escala de color logarítmica al diagrama de contenedores hexagonales estableciendo `bins='log'` en `hexbin()`.

```python
fig, ax = plt.subplots(figsize=(9, 4))

hb = ax.hexbin(x, y, gridsize=50, bins='log', cmap='inferno')
ax.set(xlim=xlim, ylim=ylim)
ax.set_title("With a log color scale")

cb = fig.colorbar(hb, ax=ax, label='log10(N)')
```
