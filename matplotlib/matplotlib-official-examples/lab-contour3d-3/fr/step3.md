# Tracez la surface 3D

Dans cette étape, nous allons tracer la surface 3D avec les données de test et personnaliser l'apparence du tracé.

```python
# Tracez la surface 3D
ax.plot_surface(X, Y, Z, edgecolor='royalblue', lw=0.5, rstride=8, cstride=8, alpha=0.3)

# Personnalisez l'apparence du tracé
ax.set(xlim=(-40, 40), ylim=(-40, 40), zlim=(-100, 100), xlabel='X', ylabel='Y', zlabel='Z')
```
