# Affichez les images dans l'ImageGrid

Enfin, nous affichons les images dans l'ImageGrid à l'aide de la fonction `imshow` et de la fonction `zip` pour itérer sur les axes de la grille.

```python
for ax, im in zip(grid, [im1, im2, im3]):
    ax.imshow(im, origin="lower", vmin=vmin, vmax=vmax)

plt.show()
```
