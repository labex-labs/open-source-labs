# Créer la figure et les sous-graphiques

Nous allons créer une figure avec deux sous-graphiques. Le premier sous-graphique sera un graphique de surface 3D, et le second sous-graphique sera un graphique en maillage 3D.

```python
# Create a figure with two subplots
fig = plt.figure(figsize=plt.figaspect(0.5))

# Add the first subplot with 3D projection
ax1 = fig.add_subplot(1, 2, 1, projection='3d')

# Add the second subplot with 3D projection
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
```
