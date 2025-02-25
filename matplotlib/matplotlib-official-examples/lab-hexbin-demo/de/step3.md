# Erstellen des hexagonalen Binned-Plots

Wir werden den hexagonalen Binned-Plot mit `matplotlib.pyplot.hexbin()` erstellen.

```python
fig, ax = plt.subplots(figsize=(9, 4))

hb = ax.hexbin(x, y, gridsize=50, cmap='inferno')
ax.set(xlim=xlim, ylim=ylim)
ax.set_title("Hexagon binning")

cb = fig.colorbar(hb, ax=ax, label='counts')
```

Hier legen wir die Gittergröße auf 50 und die Farbpalette auf 'inferno' fest. Wir fügen auch eine Farbskala hinzu, um die Anzahl der Datenpunkte in jedem Hexagon anzuzeigen.
