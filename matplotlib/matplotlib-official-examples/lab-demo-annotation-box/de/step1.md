# Punkte plotten

Beginnen wir mit dem Plotten von zwei Punkten, die wir später annotieren werden.

```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

# Definiere eine erste Position zum Annotieren (zeige sie mit einem Marker an)
xy1 = (0.5, 0.7)
ax.plot(xy1[0], xy1[1], ".r")

# Definiere eine zweite Position zum Annotieren (zeige sie diesmal nicht mit einem Marker an)
xy2 = [0.3, 0.55]

# Setze die Anzeigegrenzen, um alles zu sehen
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

plt.show()
```
