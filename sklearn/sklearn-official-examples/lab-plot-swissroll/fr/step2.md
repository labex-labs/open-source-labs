# Visualiser l'ensemble de données Swiss Roll

Nous pouvons visualiser l'ensemble de données Swiss Roll généré en utilisant un nuage de points 3D avec des couleurs différentes représentant différents points.

```python
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
fig.add_axes(ax)
ax.scatter(sr_points[:, 0], sr_points[:, 1], sr_points[:, 2], c=sr_color, s=50, alpha=0.8)
ax.set_title("Swiss Roll dans l'espace ambiant")
ax.view_init(azim=-66, elev=12)
_ = ax.text2D(0.8, 0.05, s="n_samples=1500", transform=ax.transAxes)
```
