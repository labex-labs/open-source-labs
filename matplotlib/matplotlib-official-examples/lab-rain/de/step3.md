# Den Streudiagrammplot erstellen

Jetzt werden wir den Streudiagrammplot erstellen, den wir während der Animation aktualisieren werden, wenn die Regentropfen sich entwickeln.

```python
scat = ax.scatter(rain_drops['position'][:, 0], rain_drops['position'][:, 1],
                  s=rain_drops['size'], lw=0.5, edgecolors=rain_drops['color'],
                  facecolors='none')
```
