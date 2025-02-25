# Erstellen eines Einfügebereichs außerhalb der Achse

Wir können einen Einfügebereich außerhalb der Achse erstellen, indem wir den Parameter `bbox_to_anchor` verwenden, um eine Begrenzungsbox in Achsenkoordinaten anzugeben, die außerhalb der Achse hinausreicht.

```python
# Erstellen Sie einen Einfügebereich außerhalb der Achse
axins = inset_axes(ax, width="100%", height="100%",
                   bbox_to_anchor=(1.05,.6,.5,.4),
                   bbox_transform=ax.transAxes, loc=2, borderpad=0)
```
