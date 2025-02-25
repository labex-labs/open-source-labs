# Parasitenachse anpassen

Wir müssen die Position der Parasitenachsen anpassen. Die `new_fixed_axis()`-Funktion wird verwendet, um eine neue y-Achse auf der rechten Seite des Plots zu erstellen. Die `toggle()`-Funktion wird verwendet, um alle Markierungen und Beschriftungen der rechten y-Achse anzuzeigen.

```python
par2.axis["right"] = par2.new_fixed_axis(loc="right", offset=(60, 0))

par1.axis["right"].toggle(all=True)
par2.axis["right"].toggle(all=True)
```
