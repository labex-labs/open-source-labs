# Bibliotheken importieren und Figur einrichten

Im ersten Schritt importieren wir die erforderlichen Bibliotheken und legen die Figur und Achsen für das Diagramm fest.

```python
import matplotlib.pyplot as plt
import numpy as np

# set up the figure and axes
fig = plt.figure(figsize=(8, 3))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')
```
