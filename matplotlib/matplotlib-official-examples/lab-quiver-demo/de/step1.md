# Pfeile skalieren mit der Diagrammbreite, nicht der Ansicht

Die `quiver()`-Funktion kann verwendet werden, um ein Quiver-Diagramm zu erstellen. Standardmäßig werden die Pfeile im Diagramm mit den Daten, nicht mit dem Diagramm selbst skaliert. Dies kann es schwierig machen, Pfeile zu sehen, die sich nahe am Rand des Diagramms befinden.

```python
import matplotlib.pyplot as plt
import numpy as np

X, Y = np.meshgrid(np.arange(0, 2 * np.pi,.2), np.arange(0, 2 * np.pi,.2))
U = np.cos(X)
V = np.sin(Y)

fig1, ax1 = plt.subplots()
ax1.set_title('Arrows scale with plot width, not view')
Q = ax1.quiver(X, Y, U, V, units='width')
qk = ax1.quiverkey(Q, 0.9, 0.9, 2, r'$2 \frac{m}{s}$', labelpos='E',
                   coordinates='figure')
plt.show()
```
