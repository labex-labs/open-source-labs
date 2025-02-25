# Affichez l'axe y droit du premier axe parasite

Nous affichons l'axe y droit du premier axe parasite en utilisant la méthode `par1.axis["right"].set_visible(True)`. Nous définissons également `par1.axis["right"].major_ticklabels.set_visible(True)` et `par1.axis["right"].label.set_visible(True)` pour afficher les étiquettes d'échelle et l'étiquette de l'axe y droit.

```python
par1.axis["right"].set_visible(True)
par1.axis["right"].major_ticklabels.set_visible(True)
par1.axis["right"].label.set_visible(True)
```
