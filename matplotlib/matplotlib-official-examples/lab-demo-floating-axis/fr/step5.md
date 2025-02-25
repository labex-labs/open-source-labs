# Créer des axes flottants

Dans cette étape, nous allons créer deux axes flottants qui seront utilisés pour afficher la courbe polaire dans un rectangle. Nous utiliserons `new_floating_axis()` pour créer les axes flottants.

```python
# Créer les axes flottants
ax1.axis["lat"] = axis = ax1.new_floating_axis(0, 60)
axis.label.set_text(r"$\theta = 60^{\circ}$")
axis.label.set_visible(True)

ax1.axis["lon"] = axis = ax1.new_floating_axis(1, 6)
axis.label.set_text(r"$r = 6$")
```
