# Importez les bibliothèques nécessaires et configurez le tracé

Tout d'abord, nous devons importer les bibliothèques nécessaires et configurer le tracé. Nous utiliserons `matplotlib.pyplot` et `numpy`. Nous allons également créer une figure et un objet axe pour tracer nos données dessus.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import FancyArrowPatch

fig, ax = plt.subplots()
ax.set(xlim=(0, 6), ylim=(-1, 5))
ax.set_title("Orientation des flèches croisées par rapport à angleA et angleB")
```
