# Traçage avec des marges

La méthode `margins()` dans Matplotlib peut être utilisée pour définir des marges dans le tracé au lieu d'utiliser les méthodes `set_xlim()` et `set_ylim()`. Dans cette étape, nous allons apprendre à zoomer dans et hors d'un tracé à l'aide de la méthode `margins()` au lieu des méthodes `set_xlim()` et `set_ylim()`.

```python
import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 3.0, 0.01)

# créer un sous-graphique avec des marges
ax1 = plt.subplot(212)
ax1.margins(0.05) # marge par défaut est 0.05, valeur 0 signifie ajustement
ax1.plot(t1, f(t1))

# créer un sous-graphique avec des marges élargies
ax2 = plt.subplot(221)
ax2.margins(2, 2) # valeurs >0.0 élargissent
ax2.plot(t1, f(t1))
ax2.set_title('Zoomé out')

# créer un sous-graphique avec des marges réduites
ax3 = plt.subplot(222)
ax3.margins(x=0, y=-0.25) # valeurs dans (-0.5, 0.0) zooment sur le centre
ax3.plot(t1, f(t1))
ax3.set_title('Zoomé in')

plt.show()
```
