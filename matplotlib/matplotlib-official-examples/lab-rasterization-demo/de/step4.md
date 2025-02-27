# Ein pcolormesh-Diagramm ohne Rasterisierung erstellen

Wir werden ein pcolormesh-Diagramm ohne Rasterisierung erstellen, um den Unterschied zwischen Rasterisierung und Nicht-Rasterisierung zu veranschaulichen.

```python
ax1.set_aspect(1)
ax1.pcolormesh(xx, yy, d)
ax1.set_title("No Rasterization")
```