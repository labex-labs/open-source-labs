# Créer la figure

Nous allons maintenant créer la figure en utilisant Matplotlib en ajoutant deux objets `PathPatch` à la figure. L'un sera une forme remplie d'orange, tandis que l'autre sera une bordure blanche.

```python
# Définir les limites de la figure
xmin, ymin = verts.min(axis=0) - 1
xmax, ymax = verts.max(axis=0) + 1

# Créer la figure
fig = plt.figure(figsize=(5, 5), facecolor="0.75")  # fond gris
ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1,
                  xlim=(xmin, xmax),  # centrer
                  ylim=(ymax, ymin),  # centrer, à l'envers
                  xticks=[], yticks=[])  # pas de graduations

# Ajouter la bordure blanche
ax.add_patch(patches.PathPatch(path, facecolor='none', edgecolor='w', lw=6))

# Ajouter la forme d'orange
ax.add_patch(patches.PathPatch(path, facecolor='orange', edgecolor='k', lw=2))

# Afficher la figure
plt.show()
```
