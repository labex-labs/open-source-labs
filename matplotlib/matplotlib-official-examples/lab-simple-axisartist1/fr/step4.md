# Création du deuxième sous-graphique

Dans le deuxième sous-graphique, nous allons utiliser `axisartist.axislines.AxesZero` pour créer automatiquement les axes xzero et yzero. Nous rendrons les autres épines invisibles et rendons l'axe xzero visible.

```python
ax1 = fig.add_subplot(gs[0, 1], axes_class=axisartist.axislines.AxesZero)
ax1.axis["xzero"].set_visible(True)
ax1.axis["xzero"].label.set_text("Axis Zero")
ax1.axis["bottom", "top", "right"].set_visible(False)
```
