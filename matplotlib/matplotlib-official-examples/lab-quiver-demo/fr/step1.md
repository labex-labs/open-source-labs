# Les flèches sont mises à l'échelle avec la largeur du graphique, pas la vue

La fonction `quiver()` peut être utilisée pour créer un graphique de flèches. Par défaut, les flèches dans le graphique seront mises à l'échelle avec les données, plutôt que le graphique lui-même. Cela peut rendre difficile de voir les flèches qui sont proches du bord du graphique.

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
