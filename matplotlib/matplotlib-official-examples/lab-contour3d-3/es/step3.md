# Representar la superficie 3D

En este paso, representaremos la superficie 3D con los datos de prueba y personalizaremos la apariencia de la representación.

```python
# Representa la superficie 3D
ax.plot_surface(X, Y, Z, edgecolor='royalblue', lw=0.5, rstride=8, cstride=8, alpha=0.3)

# Personaliza la apariencia de la representación
ax.set(xlim=(-40, 40), ylim=(-40, 40), zlim=(-100, 100), xlabel='X', ylabel='Y', zlabel='Z')
```
