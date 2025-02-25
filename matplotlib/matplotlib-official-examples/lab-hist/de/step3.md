# Zeichnen eines 2D-Histogramms

Um ein 2D-Histogramm zu zeichnen, benötigt man nur zwei Vektoren von gleicher Länge, die jeweils einer Achse des Histogramms entsprechen.

```python
fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(dist1, dist2)

plt.show()
```
