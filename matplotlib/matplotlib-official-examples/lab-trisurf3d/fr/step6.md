# Créer la surface 3D

Nous allons créer la surface 3D à l'aide de la fonction `plot_trisurf` :

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)

plt.show()
```
