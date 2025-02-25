# Définir la fonction d'ajout d'un axe flottant

Définissez la fonction `add_floating_axis`, qui ajoute un axe flottant au graphique. Cette fonction prend en argument l'objet `ax1` et renvoie l'objet `axis`.

```python
def add_floating_axis(ax1):
    # Définir l'axe flottant
    ax1.axis["lat"] = axis = ax1.new_floating_axis(0, 30)
    axis.label.set_text(r"$\theta = 30^{\circ}$")
    axis.label.set_visible(True)

    return axis
```
