# Farbskala und Erweiterungseinstellungen festlegen

Schließlich werden wir die Farbskala und die Erweiterungseinstellungen festlegen. Wir verwenden die `with_extremes`-Methode, um die Farben für Werte unterhalb und überhalb des Bereichs der Ebenen festzulegen. Wir erstellen auch vier Teilplots, um die vier möglichen `extend`-Einstellungen zu zeigen: `'neither'`, `'both'`, `'min'` und `'max'`.

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
