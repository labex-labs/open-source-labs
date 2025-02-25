# Bords collants

Certaines fonctions de tracé dans Matplotlib rendent les limites de l'axe "collantes" ou immunes à la méthode `margins()`. Par exemple, `imshow()` et `pcolor()` supposent que l'utilisateur souhaite que les limites soient strictes autour des pixels affichés dans le tracé. Si ce comportement n'est pas souhaité, vous devez définir `use_sticky_edges` sur `False`. Dans cette étape, nous allons apprendre à contourner les bords collants dans Matplotlib.

```python
# créer une grille
y, x = np.mgrid[:5, 1:6]

# définir les coordonnées du polygone
poly_coords = [
    (0.25, 2.75), (3.25, 2.75),
    (2.25, 0.75), (0.25, 0.75)
]

# créer des sous-graphiques
fig, (ax1, ax2) = plt.subplots(ncols=2)

# utiliser des bords collants pour ax1 et désactiver les bords collants pour ax2
ax2.use_sticky_edges = False

# tracer sur les deux sous-graphiques
for ax, status in zip((ax1, ax2), ('Est', 'N\'est pas')):
    cells = ax.pcolor(x, y, x+y, cmap='inferno', shading='auto') # collant
    ax.add_patch(
        Polygon(poly_coords, color='forestgreen', alpha=0.5)
    ) # non collant
    ax.margins(x=0.1, y=0.05)
    ax.set_aspect('equal')
    ax.set_title(f'{status} Collant')

plt.show()
```
