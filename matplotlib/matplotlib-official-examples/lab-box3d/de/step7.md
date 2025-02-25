# Zoom- und Blickwinkel einstellen

Stellen Sie den Zoom und den Blickwinkel mit den Methoden `view_init` und `set_box_aspect` ein. Wir werden den Blickwinkel in X-Richtung auf 40 Grad und in Y-Richtung auf -30 Grad einstellen und den Zoom auf 0,9.

```python
# Set zoom and angle view
ax.view_init(40, -30, 0)
ax.set_box_aspect(None, zoom=0.9)
```
