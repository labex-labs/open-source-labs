# Personnaliser le tracé

Nous pouvons personnaliser le tracé en ajoutant des étiquettes aux axes et en ajustant l'angle de visualisation.

```python
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.view_init(elev=30, azim=120)
```
