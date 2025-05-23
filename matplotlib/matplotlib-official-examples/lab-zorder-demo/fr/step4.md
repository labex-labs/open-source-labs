# Ordre personnalisé d'éléments

Nous pouvons également définir le `zorder` des éléments dans un ordre personnalisé. Par exemple, nous pouvons définir le `zorder` d'une légende pour qu'elle soit située entre deux lignes.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 7.5, 100)
plt.rcParams['lines.linewidth'] = 5
plt.figure()
plt.plot(x, np.sin(x), label='zorder=2', zorder=2)  # en bas
plt.plot(x, np.sin(x+0.5), label='zorder=3',  zorder=3)
plt.axhline(0, label='zorder=2.5', color='lightgrey', zorder=2.5)
plt.title('Ordre personnalisé d\'éléments')
l = plt.legend(loc='upper right')
l.set_zorder(2.5)  # légende entre la ligne bleue et l'orange
plt.show()
```
