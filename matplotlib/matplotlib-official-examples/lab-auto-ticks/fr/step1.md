# Diagramme en points sans mode d'autolimitation round_numbers

Dans cette étape, nous allons créer un diagramme en points sans le mode d'autolimitation round_numbers et observer le comportement du positionnement automatique des graduations.

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

fig, ax = plt.subplots()
dots = np.linspace(0.3, 1.2, 10)
X, Y = np.meshgrid(dots, dots)
x, y = X.ravel(), Y.ravel()
ax.scatter(x, y, c=x+y)
plt.show()
```
