# Ajout d'un axe flottant

Nous allons définir deux fonctions qui ajouteront des axes flottants à notre tracé. La première fonction `add_floating_axis1()` ajoute un axe flottant au tracé avec une étiquette de `theta = 30`. La deuxième fonction `add_floating_axis2()` ajoute un axe flottant au tracé avec une étiquette de `r = 6`.

```python
def add_floating_axis1(ax):
    ax.axis["lat"] = axis = ax.new_floating_axis(0, 30)
    axis.label.set_text(r"$\theta = 30^{\circ}$")
    axis.label.set_visible(True)
    return axis

def add_floating_axis2(ax):
    ax.axis["lon"] = axis = ax.new_floating_axis(1, 6)
    axis.label.set_text(r"$r = 6$")
    axis.label.set_visible(True)
    return axis
```
