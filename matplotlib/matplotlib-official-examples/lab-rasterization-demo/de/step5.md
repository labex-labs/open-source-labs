# Ein pcolormesh-Diagramm mit Rasterisierung erstellen

Wir werden ein pcolormesh-Diagramm mit Rasterisierung erstellen, um zu veranschaulichen, wie die Rasterisierung die Rendering-Geschwindigkeit erhöhen und kleinere Dateien erzeugen kann.

```python
ax2.set_aspect(1)
ax2.set_title("Rasterization")
ax2.pcolormesh(xx, yy, d, rasterized=True)
```