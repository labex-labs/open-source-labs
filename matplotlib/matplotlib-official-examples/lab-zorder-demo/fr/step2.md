# Changer zorder

Pour changer l'ordre de tracé des artistes, nous pouvons définir explicitement leur attribut `zorder` en utilisant le paramètre `zorder` lors de la création de l'artiste. Par exemple, nous pouvons déplacer les points au-dessus des lignes dans un nuage de points en définissant le `zorder` des points sur une valeur supérieure au `zorder` de la ligne.

```python
import matplotlib.pyplot as plt
import numpy as np

r = np.linspace(0.3, 1, 30)
theta = np.linspace(0, 4*np.pi, 30)
x = r * np.sin(theta)
y = r * np.cos(theta)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3.2))

ax1.plot(x, y, 'C3', lw=3)
ax1.scatter(x, y, s=120)
ax1.set_title('Lignes au-dessus des points')

ax2.plot(x, y, 'C3', lw=3)
ax2.scatter(x, y, s=120, zorder=2.5)  # déplacer les points au-dessus de la ligne
ax2.set_title('Points au-dessus des lignes')

plt.tight_layout()
plt.show()
```
