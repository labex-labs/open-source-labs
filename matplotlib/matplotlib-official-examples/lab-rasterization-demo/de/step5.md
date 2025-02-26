# Erstellen eines pcolormesh-Diagramms mit Ver光栅isierung

Wir werden ein pcolormesh-Diagramm mit Ver光栅isierung erstellen, um zu veranschaulichen, wie die Ver光栅isierung die Wiedergabe beschleunigen und kleinere Dateien erzeugen kann.

```python
ax2.set_aspect(1)
ax2.set_title("Ver光栅isierung")
ax2.pcolormesh(xx, yy, d, rasterized=True)
```