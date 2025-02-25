# Erstellen der Hauptachsen

In diesem Schritt werden wir die Hauptachsen erstellen und das Grid-Hilfsmittel festlegen. Wir werden `fig.add_subplot()` verwenden, um die Hauptachsen zu erstellen.

```python
# Erstellen der Hauptachsen
fig = plt.figure(figsize=(5, 5))
ax1 = fig.add_subplot(axes_class=HostAxes, grid_helper=grid_helper)
```
