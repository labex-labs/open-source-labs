# Anpassen Ihres Histogramms

Das Anpassen eines 2D-Histogramms ähnelt dem eindimensionalen Fall. Sie können visuelle Komponenten wie die Bin-Größe oder die Farbnormalisierung steuern.

```python
fig, axs = plt.subplots(3, 1, figsize=(5, 15), sharex=True, sharey=True,
                        tight_layout=True)

# Wir können die Anzahl der Bins auf jeder Achse erhöhen
axs[0].hist2d(dist1, dist2, bins=40)

# Ebenso können wir die Normalisierung der Farben definieren
axs[1].hist2d(dist1, dist2, bins=40, norm=colors.LogNorm())

# Wir können auch benutzerdefinierte Bin-Zahlen für jede Achse definieren
axs[2].hist2d(dist1, dist2, bins=(80, 10), norm=colors.LogNorm())

plt.show()
```
