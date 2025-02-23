# Importieren der erforderlichen Bibliotheken und Einrichten des Diagramms

Zunächst müssen wir die erforderlichen Bibliotheken importieren und das Diagramm einrichten. Wir werden `matplotlib.pyplot` und `numpy` verwenden. Wir werden auch ein Figure- und ein Axes-Objekt erstellen, um unsere Daten darauf zu plotten.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import FancyArrowPatch

fig, ax = plt.subplots()
ax.set(xlim=(0, 6), ylim=(-1, 5))
ax.set_title("Orientation of the bracket arrows relative to angleA and angleB")
```
