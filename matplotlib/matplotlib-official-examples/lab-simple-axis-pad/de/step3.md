# Definiere die Funktion zum Hinzufügen einer fließenden Achse

Definiere die `add_floating_axis`-Funktion, die einer Grafik eine fließende Achse hinzufügt. Diese Funktion nimmt das `ax1`-Objekt als Argument entgegen und gibt das `axis`-Objekt zurück.

```python
def add_floating_axis(ax1):
    # Definiere die fließende Achse
    ax1.axis["lat"] = axis = ax1.new_floating_axis(0, 30)
    axis.label.set_text(r"$\theta = 30^{\circ}$")
    axis.label.set_visible(True)

    return axis
```
