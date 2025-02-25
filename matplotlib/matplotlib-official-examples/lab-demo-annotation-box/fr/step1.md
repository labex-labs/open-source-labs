# Tracer des points

Pour commencer, traçons deux points que nous annoterons plus tard.

```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

# Définissez une première position à annoter (affichez-la avec un marqueur)
xy1 = (0.5, 0.7)
ax.plot(xy1[0], xy1[1], ".r")

# Définissez une deuxième position à annoter (ne l'affichez pas avec un marqueur cette fois)
xy2 = [0.3, 0.55]

# Fixez les limites d'affichage pour voir tout
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

plt.show()
```
