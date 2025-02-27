# Erstellen eines pcolormesh-Plots ohne Ver光栅isierung

Wir werden einen pcolormesh-Plot ohne Ver光栅isierung erstellen, um den Unterschied zwischen Ver光栅isierung und Nicht-Ver光栅isierung zu veranschaulichen.

```python
ax1.set_aspect(1)
ax1.pcolormesh(xx, yy, d)
ax1.set_title("No Rasterization")
```