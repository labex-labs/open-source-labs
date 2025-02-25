# Direction personnalisée des étiquettes d'échelle

Dans cette étape, nous allons créer un sous-graphique avec une direction personnalisée pour les étiquettes d'échelle.

```python
ax = setup_axes(fig, 132)
ax.axis["left"].set_axis_direction("right")
ax.axis["bottom"].set_axis_direction("top")
ax.axis["right"].set_axis_direction("left")
ax.axis["top"].set_axis_direction("bottom")
```
