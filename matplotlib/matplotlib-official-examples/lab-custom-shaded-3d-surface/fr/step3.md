# Personnaliser l'ombrage

Dans cette étape, nous allons personnaliser l'ombrage en remplaçant l'ombrage intégré et en passant les couleurs RGB de la surface ombrée calculées à partir de "shade".

```python
# Préparer le tracé
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))

ls = LightSource(270, 45)
# Pour utiliser un mode d'ombrage personnalisé, remplacer l'ombrage intégré et passer
# les couleurs rgb de la surface ombrée calculées à partir de "shade".
rgb = ls.shade(z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=rgb,
                       linewidth=0, antialiased=False, shade=False)

plt.show()
```
