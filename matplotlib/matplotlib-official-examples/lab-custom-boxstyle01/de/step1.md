# Implementieren eines benutzerdefinierten Box-Stils als Funktion

Benutzerdefinierte Box-Stile können als Funktionen implementiert werden, die Argumente übergeben bekommen, die sowohl eine rechteckige Box als auch die Größe der „Mutation“ angeben, und den „mutierten“ Pfad zurückgeben. Hier implementieren wir einen benutzerdefinierten Box-Stil, der einen neuen Pfad zurückgibt, der links von der Box eine „Pfeil“-Form hinzufügt.

```python
import matplotlib.pyplot as plt
from matplotlib.patches import BoxStyle
from matplotlib.path import Path

def custom_box_style(x0, y0, width, height, mutation_size):
    """
    Gegeben die Position und Größe der Box, gibt den Pfad der Box um sie herum zurück.

    Die Rotation wird automatisch übernommen.

    Parameter
    ----------
    x0, y0, width, height : float
        Box-Position und -Größe.
    mutation_size : float
        Mutationsreferenzmaßstab, typischerweise die Text-Schriftgröße.
    """
    # Padding
    mypad = 0.3
    pad = mutation_size * mypad
    # Breite und Höhe mit hinzugefügtem Padding.
    width = width + 2 * pad
    height = height + 2 * pad
    # Grenze der gepaddeten Box
    x0, y0 = x0 - pad, y0 - pad
    x1, y1 = x0 + width, y0 + height
    # Gebe den neuen Pfad zurück
    return Path([(x0, y0),
                 (x1, y0), (x1, y1), (x0, y1),
                 (x0-pad, (y0+y1)/2), (x0, y0),
                 (x0, y0)],
                closed=True)

fig, ax = plt.subplots(figsize=(3, 3))
ax.text(0.5, 0.5, "Test", size=30, va="center", ha="center", rotation=30,
        bbox=dict(boxstyle=custom_box_style, alpha=0.2))
plt.show()
```
