# Préparer le tracé

Dans cette étape, nous allons préparer le tracé pour le tracé de surface 3D. Nous utiliserons un objet LightSource pour personnaliser l'ombrage.

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
