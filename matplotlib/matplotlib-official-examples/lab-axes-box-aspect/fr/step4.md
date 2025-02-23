# Graphique normal à côté d'une image

Lors de la création d'un graphique d'image avec un aspect de données fixe et la valeur par défaut `adjustable="box"` à côté d'un graphique normal, les axes auraient des hauteurs inégales. `set_box_aspect()` fournit une solution simple à ce problème en permettant aux axes du graphique normal d'utiliser les dimensions de l'image comme aspect de la boîte. Cet exemple montre également que la mise en page contraignue interagit bien avec un aspect de boîte fixe.

```python
fig4, (ax, ax2) = plt.subplots(ncols=2, layout="constrained")

np.random.seed(19680801)  # Fixing random state for reproducibility
im = np.random.rand(16, 27)
ax.imshow(im)

ax2.plot([23, 45])
ax2.set_box_aspect(im.shape[0]/im.shape[1])

plt.show()
```
