# Créez le graphique

Nous allons créer le graphique en calculant d'abord l'image à l'aide de la classe MandelbrotDisplay, puis en créant deux panneaux identiques à l'aide de subplots. Nous ajouterons l'image à both panels à l'aide de imshow, et ajouterons l'objet UpdatingRect au panneau gauche.

```python
md = MandelbrotDisplay()
Z = md.compute_image(-2., 0.5, -1.25, 1.25)

fig1, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(Z, origin='lower',
           extent=(md.x.min(), md.x.max(), md.y.min(), md.y.max()))
ax2.imshow(Z, origin='lower',
           extent=(md.x.min(), md.x.max(), md.y.min(), md.y.max()))

rect = UpdatingRect(
    [0, 0], 0, 0, facecolor='none', edgecolor='black', linewidth=1.0)
rect.set_bounds(*ax2.viewLim.bounds)
ax1.add_patch(rect)
```
