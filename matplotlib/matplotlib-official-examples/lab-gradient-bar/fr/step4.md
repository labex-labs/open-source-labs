# Définissez la fonction de barre à gradient

Ensuite, nous devons définir une fonction qui créera une barre à gradient. Cette fonction prendra l'objet d'axes, les coordonnées x et y de la barre, la largeur de la barre et la position du bas de la barre. La fonction créera ensuite une image à gradient pour chaque barre et la renverra.

```python
def gradient_bar(ax, x, y, width=0.5, bottom=0):
    for left, top in zip(x, y):
        right = left + width
        gradient_image(ax, extent=(left, right, bottom, top),
                       cmap=plt.cm.Blues_r, cmap_range=(0, 0.8))
```
