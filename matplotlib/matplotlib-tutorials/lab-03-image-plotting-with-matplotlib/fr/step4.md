# Ajout d'une référence d'échelle de couleur

Pour fournir une référence pour l'échelle de couleur, nous pouvons ajouter une barre de couleur au tracé. Cela peut être fait à l'aide de la fonction `colorbar` de `matplotlib.pyplot`.

```python
imgplot = plt.imshow(lum_img)
plt.colorbar()
```
