# Erstellen des Matplotlib-Diagramms

In diesem Schritt werden wir ein Matplotlib-Diagramm erstellen, das unsere Daten anzeigt. Wir beginnen damit, eine Figur zu erstellen und ein Subplot hinzuzufügen.

```python
fig = Figure(figsize=(6, 4))
self.canvas = FigureCanvas(fig)
vbox.pack_start(self.canvas, True, True, 0)
ax = fig.add_subplot()
```
