# Erstellen der schrägen Trennlinien

Schließlich werden wir die schrägen Trennlinien erstellen. Wir werden Linienobjekte in Achsenkoordinaten erstellen und `ax1.transAxes` und `ax2.transAxes` verwenden, um sie in die Koordinaten jedes Teilplots (Subplots) zu transformieren. Wir verwenden `ax1.plot` und `ax2.plot`, um die Linien zu zeichnen. Wir verwenden auch `marker`, um den Markierungsstil anzugeben, `markersize`, um die Größe der Marker festzulegen, `linestyle`, um den Stil der Linie festzulegen, `color`, um die Farbe der Linie festzulegen, `mec`, um die Farbe des Markerrandes festzulegen, und `mew`, um die Breite des Markerrandes festzulegen.

```python
d =.5
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)
```
