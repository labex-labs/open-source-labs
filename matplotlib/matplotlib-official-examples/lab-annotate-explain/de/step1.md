# Plot einrichten

Zunächst müssen wir den Plot mit zwei Teilplots einrichten. Wir werden die `subplots`-Funktion verwenden, um ein 2x2-Gitter von Teilplots zu erstellen, und dann definieren wir die x- und y-Koordinaten zweier Punkte.

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, axs = plt.subplots(2, 2)
x1, y1 = 0.3, 0.3
x2, y2 = 0.7, 0.7
```
