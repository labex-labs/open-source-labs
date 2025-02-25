# Definiere die Achsenpositionen mit einem gridspec

Wir werden nun ein `gridspec` mit ungleichen Breiten- und Höhenverhältnissen definieren, um das gewünschte Layout zu erreichen. Wir werden auch die Achsen erstellen und sie an die `scatter_hist`-Funktion übergeben.

```python
# Beginne mit einer quadratischen Figur.
fig = plt.figure(figsize=(6, 6))
# Füge ein gridspec mit zwei Zeilen und zwei Spalten und einem Verhältnis von 1 zu 4 zwischen
# der Größe der Randachsen und der Hauptachsen in beiden Richtungen hinzu.
# Passt auch die Subplot-Parameter für ein quadratisches Diagramm an.
gs = fig.add_gridspec(2, 2,  width_ratios=(4, 1), height_ratios=(1, 4),
                      left=0.1, right=0.9, bottom=0.1, top=0.9,
                      wspace=0.05, hspace=0.05)
# Erstelle die Achsen.
ax = fig.add_subplot(gs[1, 0])
ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)
ax_histy = fig.add_subplot(gs[1, 1], sharey=ax)
# Zeichne das Streudiagramm und die Marginalien.
scatter_hist(x, y, ax, ax_histx, ax_histy)
```
