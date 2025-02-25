# Créer un deuxième axe y

Enfin, nous allons créer un deuxième axe y sur le côté droit du graphique avec un décalage de (20, 0) et lui attribuer une étiquette.

```python
ax.axis["right2"] = ax.new_fixed_axis(loc="right", offset=(20, 0))
ax.axis["right2"].label.set_text("Label Y2")
```
