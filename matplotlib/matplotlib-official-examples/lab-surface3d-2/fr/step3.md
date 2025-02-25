# Création du tracé de surface 3D

Maintenant, nous pouvons créer le tracé de surface 3D. Nous commençons par créer une figure et en ajoutant un sous-graphique avec l'argument `projection='3d'`. Ensuite, nous utilisons la fonction `plot_surface()` pour tracer la surface à l'aide des données que nous avons créées dans l'étape précédente.

```python
# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z)
```
