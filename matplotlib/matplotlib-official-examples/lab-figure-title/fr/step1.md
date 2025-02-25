# Créez un tracé d'oscillation amortie et non amortie

Tout d'abord, nous allons créer une figure avec deux sous-graphiques, l'un pour une oscillation amortie et l'autre pour une oscillation non amortie. Nous utiliserons la fonction `np.linspace()` pour créer un tableau de valeurs de temps puis tracer les valeurs d'amplitude correspondantes pour chaque type d'oscillation à l'aide des fonctions `np.cos()` et `np.exp()`.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 5.0, 501)

fig, (ax1, ax2) = plt.subplots(1, 2, layout='constrained', sharey=True)
ax1.plot(x, np.cos(6*x) * np.exp(-x))
ax1.set_title('amortie')
ax1.set_xlabel('temps (s)')
ax1.set_ylabel('amplitude')

ax2.plot(x, np.cos(6*x))
ax2.set_xlabel('temps (s)')
ax2.set_title('non amortie')

fig.suptitle('Différents types d'oscillations', fontsize=16)

plt.show()
```
