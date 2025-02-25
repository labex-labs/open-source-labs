# Traçage du graphique en voxels

Enfin, nous pouvons tracer le graphique en voxels en utilisant la fonction `ax.voxels`. Nous passerons les valeurs RGB, la condition pour la sphère, les couleurs des faces, les couleurs des bords et la largeur de ligne.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(r, g, b, sphere,
          facecolors=colors,
          edgecolors=np.clip(2*colors - 0.5, 0, 1),  # plus clair
          linewidth=0.5)
ax.set(xlabel='r', ylabel='g', zlabel='b')
ax.set_aspect('equal')
plt.show()
```
