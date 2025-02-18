# Manuelle Y-Positionierung

Geben Sie manuell die vertikale Position des Titels an, indem Sie den Parameter `y` der Funktion `title()` verwenden.

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.xaxis.set_label_position('top')
ax.set_xlabel('X-label')
ax.set_title('Manual Y Positioning', y=1.0)
```
