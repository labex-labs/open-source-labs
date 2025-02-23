# Configure le graphique

Tout d'abord, nous devons configurer le graphique avec deux sous-graphiques. Nous allons utiliser la fonction `subplots` pour créer une grille 2x2 de sous-graphiques, puis nous définirons les coordonnées x et y de deux points.

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, axs = plt.subplots(2, 2)
x1, y1 = 0.3, 0.3
x2, y2 = 0.7, 0.7
```
