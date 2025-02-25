# Tracer la surface

Dans cette étape, nous allons tracer la surface à l'aide de la fonction `plot_surface()` de Matplotlib. Nous utiliserons la carte de couleurs `YlGnBu_r` pour définir la couleur de la surface.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)
```
