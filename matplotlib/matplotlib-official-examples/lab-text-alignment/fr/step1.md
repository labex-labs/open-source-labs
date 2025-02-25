# Création d'un rectangle

Nous allons commencer par créer un rectangle dans le tracé à l'aide de la fonction `Rectangle()` du module `matplotlib.patches`. Après avoir créé le rectangle, nous allons définir ses limites horizontales et verticales à l'aide des fonctions `set_xlim()` et `set_ylim()`. Enfin, nous ajouterons le rectangle au tracé.

```python
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots()

# Build a rectangle in axes coords
left, width =.25,.5
bottom, height =.25,.5
right = left + width
top = bottom + height
p = Rectangle((left, bottom), width, height, fill=False)
ax.add_patch(p)

# Set the horizontal and vertical limits
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.show()
```
