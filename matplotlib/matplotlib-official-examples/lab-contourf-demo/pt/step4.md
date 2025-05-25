# Definir Mapa de Cores (Colormap) e Configurações de Extensão

Finalmente, definiremos o mapa de cores (colormap) e as configurações de extensão. Usaremos o método `with_extremes` para definir as cores para valores abaixo e acima da faixa de níveis. Também criaremos quatro subplots para mostrar as quatro configurações de `extend` possíveis: `'neither'`, `'both'`, `'min'` e `'max'`.

```python
# Set colormap and extend settings
extends = ["neither", "both", "min", "max"]
cmap = plt.colormaps["winter"].with_extremes(under="magenta", over="yellow")

# Create subplots with different extend settings
fig, axs = plt.subplots(2, 2, layout="constrained")
for ax, extend in zip(axs.flat, extends):
    cs = ax.contourf(X, Y, Z, levels, cmap=cmap, extend=extend, origin=origin)
    fig.colorbar(cs, ax=ax, shrink=0.9)
    ax.set_title("extend = %s" % extend)
    ax.locator_params(nbins=4)

# Show plot
plt.show()
```
