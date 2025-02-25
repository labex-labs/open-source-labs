# Itérez sur la grille et tracez les images

Ensuite, nous itérons sur l'objet `grid` à l'aide de la fonction `zip` pour itérer à la fois sur les axes et les tableaux d'images. Nous traçons chaque image sur son axe correspondant à l'aide de la fonction `imshow`.

```python
for ax, im in zip(grid, [im1, im2, im3, im4]):
    ax.imshow(im)
```
