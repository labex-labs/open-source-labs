# Definir la función scatter_hist

Necesitamos definir la función `scatter_hist`, que toma los datos x e y, así como tres ejes: el eje principal para el diagrama de dispersión y dos ejes marginales. Luego creará el diagrama de dispersión y los histogramas dentro de los ejes proporcionados.

```python
def scatter_hist(x, y, ax, ax_histx, ax_histy):
    # Remove labels from the histograms
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histy.tick_params(axis="y", labelleft=False)

    # Create the scatter plot
    ax.scatter(x, y)

    # Determine nice limits by hand
    binwidth = 0.25
    xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
    lim = (int(xymax/binwidth) + 1) * binwidth

    bins = np.arange(-lim, lim + binwidth, binwidth)
    ax_histx.hist(x, bins=bins)
    ax_histy.hist(y, bins=bins, orientation='horizontal')
```
