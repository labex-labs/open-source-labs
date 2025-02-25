# Aktualisieren der Histogramm-Farben

Die `histogram`-Methode gibt (unter anderem) ein `patches`-Objekt zurück. Dies ermöglicht uns den Zugang zu den Eigenschaften der gezeichneten Objekte. Mit diesem können wir das Histogramm nach unseren Wünschen bearbeiten. Ändern wir die Farbe jeder Säule basierend auf ihrem y-Wert.

```python
# N ist die Anzahl in jedem Bin, bins ist der untere Grenzwert des Bins
N, bins, patches = axs[0].hist(dist1, bins=n_bins)

# Wir werden die Farben nach der Höhe kodieren, aber Sie könnten auch jedes Skalar verwenden
fracs = N / N.max()

# Wir müssen die Daten auf den Bereich 0..1 normalisieren, um die volle Palette der Farbkarte zu nutzen
norm = colors.Normalize(fracs.min(), fracs.max())

# Nun durchlaufen wir unsere Objekte und setzen die Farbe jedes entsprechend
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)

# Wir können unsere Eingaben auch durch die Gesamtanzahl der Zählungen normalisieren
axs[1].hist(dist1, bins=n_bins, density=True)

# Nun formatieren wir die y-Achse, um Prozentangaben anzuzeigen
axs[1].yaxis.set_major_formatter(PercentFormatter(xmax=1))

plt.show()
```
