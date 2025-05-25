# Configurando o Gráfico

Em seguida, configuraremos o gráfico criando uma figura e um array de subplots. Também definiremos uma função `setup` que define parâmetros comuns para os eixos no exemplo.

```python
fig, axs = plt.subplots(8, 1, figsize=(8, 6))

def setup(ax, title):
    """Define parâmetros comuns para os Axes no exemplo."""
    # mostra apenas a borda inferior
    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.spines[['left', 'right', 'top']].set_visible(False)

    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(which='major', width=1.00, length=5)
    ax.tick_params(which='minor', width=0.75, length=2.5)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1)
    ax.text(0.0, 0.2, title, transform=ax.transAxes,
            fontsize=14, fontname='Monospace', color='tab:blue')
```
