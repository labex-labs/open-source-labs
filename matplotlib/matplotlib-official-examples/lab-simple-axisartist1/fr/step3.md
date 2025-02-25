# Création du premier sous-graphique

Dans le premier sous-graphique, nous allons créer un nouvel axe qui passe par y = 0 en utilisant `axisartist.Axes`. Nous rendrons également les autres épines invisibles.

```python
ax0 = fig.add_subplot(gs[0, 0], axes_class=axisartist.Axes)
ax0.axis["y=0"] = ax0.new_floating_axis(nth_coord=0, value=0, axis_direction="bottom")
ax0.axis["y=0"].toggle(all=True)
ax0.axis["y=0"].label.set_text("y = 0")
ax0.axis["bottom", "top", "right"].set_visible(False)
```
