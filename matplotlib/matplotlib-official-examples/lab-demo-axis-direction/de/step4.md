# Ändern der Achsenrichtung

Jetzt erstellen wir eine Schleife, um vier verschiedene Diagramme mit der fließenden Achse in jeder der vier Hauptrichtungen einzurichten. In der Schleife verwenden wir `add_floating_axis1()` und `add_floating_axis2()`, um die fließenden Achsen hinzuzufügen, und `set_axis_direction()`, um die Achsenrichtung festzulegen.

```python
fig = plt.figure(figsize=(8, 4), layout="constrained")

for i, d in enumerate(["bottom", "left", "top", "right"]):
    ax = setup_axes(fig, rect=241+i)
    axis = add_floating_axis1(ax)
    axis.set_axis_direction(d)
    ax.set(title=d)

for i, d in enumerate(["bottom", "left", "top", "right"]):
    ax = setup_axes(fig, rect=245+i)
    axis = add_floating_axis2(ax)
    axis.set_axis_direction(d)
    ax.set(title=d)

plt.show()
```
