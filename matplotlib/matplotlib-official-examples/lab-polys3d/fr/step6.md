# Créez les polygones et ajoutez-les au tracé

Nous créons les polygones à l'aide de la fonction `PolyCollection` de Matplotlib et les ajoutons au tracé.

```python
poly = PolyCollection(verts, facecolors=facecolors, alpha=.7)
ax.add_collection3d(poly, zs=lambdas, zdir='y')
```
