# Créer un tracé 3D

Ensuite, nous allons créer un tracé 3D à l'aide des fonctions `plt.figure()` et `fig.add_subplot()`. Nous utiliserons également la fonction `ax.plot_wireframe()` pour tracer l'ensemble de données sous forme d'un cadre de fils.

```python
# Créer un tracé 3D
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Tracer le cadre de fils
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```
