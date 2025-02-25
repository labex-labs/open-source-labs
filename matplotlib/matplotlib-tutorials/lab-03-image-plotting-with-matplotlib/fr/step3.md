# Application de schémas de pseudocolor

Les schémas de pseudocolor peuvent être utilisés pour améliorer le contraste et visualiser les données plus facilement. Si l'image est en niveaux de gris, nous pouvons appliquer des schémas de pseudocolor en spécifiant différents cartes de couleurs. Nous pouvons le faire en utilisant le paramètre `cmap` dans la fonction `imshow`.

```python
lum_img = img[:, :, 0]
plt.imshow(lum_img, cmap="hot")
```
