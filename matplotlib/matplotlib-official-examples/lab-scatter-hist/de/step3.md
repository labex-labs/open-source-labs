# Definiere die scatter_hist-Funktion

Wir müssen die `scatter_hist`-Funktion definieren, die x- und y-Daten sowie drei Achsen annimmt: die Hauptachse für das Streudiagramm und zwei Randachsen. Anschließend wird das Streudiagramm und die Histogramme innerhalb der bereitgestellten Achsen erstellt.

```python
def scatter_hist(x, y, ax, ax_histx, ax_histy):
    # Entferne die Beschriftungen von den Histogrammen
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histy.tick_params(axis="y", labelleft=False)

    # Erstelle das Streudiagramm
    ax.scatter(x, y)

    # Bestimme schöne Grenzen manuell
    binwidth = 0.25
    xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
    lim = (int(xymax/binwidth) + 1) * binwidth

    bins = np.arange(-lim, lim + binwidth, binwidth)
    ax_histx.hist(x, bins=bins)
    ax_histy.hist(y, bins=bins, orientation='horizontal')
```
