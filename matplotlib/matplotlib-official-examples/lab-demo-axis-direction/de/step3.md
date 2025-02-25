# Hinzufügen von fließenden Achsen

Wir werden zwei Funktionen definieren, die fließende Achsen zu unserem Diagramm hinzufügen. Die erste Funktion `add_floating_axis1()` fügt einer Achse mit dem Label `theta = 30` hinzu. Die zweite Funktion `add_floating_axis2()` fügt einer Achse mit dem Label `r = 6` hinzu.

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
