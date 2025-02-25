# Funktion für Fehlerboxen erstellen

Wir werden nun eine Funktion namens `make_error_boxes` erstellen, die den Rechteck-Patch erstellt, der durch die Grenzen der Balken in beiden x- und y-Richtungen definiert ist.

```python
def make_error_boxes(ax, xdata, ydata, xerror, yerror, facecolor='r',
                     edgecolor='none', alpha=0.5):

    # Schleife über die Datenpunkte; erstelle Box aus Fehlern an jedem Punkt
    errorboxes = [Rectangle((x - xe[0], y - ye[0]), xe.sum(), ye.sum())
                  for x, y, xe, ye in zip(xdata, ydata, xerror.T, yerror.T)]

    # Erstelle Patch-Collection mit der angegebenen Farbe/Alpha
    pc = PatchCollection(errorboxes, facecolor=facecolor, alpha=alpha,
                         edgecolor=edgecolor)

    # Füge die Collection zur Achse hinzu
    ax.add_collection(pc)

    # Plotte die Fehlerbalken
    artists = ax.errorbar(xdata, ydata, xerr=xerror, yerr=yerror,
                          fmt='none', ecolor='k')

    return artists
```
