# Définition des axes et affichage de l'image

La quatrième étape consiste à définir les axes à l'aide de l'instance `grid_helper` créée à l'étape 3. Nous afficherons également une image à l'aide de la fonction `imshow`.

```python
ax1 = fig.add_subplot(axes_class=Axes, grid_helper=grid_helper)
ax1.imshow(np.arange(25).reshape(5, 5), vmax=50, cmap=plt.cm.gray_r, origin="lower")
```
