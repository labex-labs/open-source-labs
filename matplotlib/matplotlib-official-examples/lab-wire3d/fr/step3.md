# Créer le tracé

Maintenant que nous avons nos données, nous pouvons créer le tracé de trame. Dans cet exemple, nous utiliserons la fonction `plot_wireframe()` pour créer le tracé.

```python
# Créer le tracé
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)
```
