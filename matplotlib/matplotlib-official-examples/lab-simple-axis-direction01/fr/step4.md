# Définir les étiquettes des axes

Nous définissons les étiquettes des axes pour les côtés gauche et droit du tracé à l'aide de la fonction `ax1.axis[]`. Nous définissons également la direction des étiquettes d'échelle à l'aide de la fonction `set_axis_direction()`.

```python
ax1.axis["left"].major_ticklabels.set_axis_direction("top")
ax1.axis["left"].label.set_text("Étiquette gauche")

ax1.axis["right"].label.set_visible(True)
ax1.axis["right"].label.set_text("Étiquette droite")
ax1.axis["right"].label.set_axis_direction("left")
```
