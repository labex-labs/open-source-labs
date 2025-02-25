# Erstellen eines gruppierten Balkendiagramms

Jetzt können wir unser Diagramm mit der `bar`-Funktion aus Matplotlib erstellen. Wir werden eine Schleife erstellen, die durch unsere Attribute iteriert und für jedes Attribut einen Satz von Balken erstellt. Wir werden auch die Breite der Balken und die Position jedes Satzes von Balken anpassen.

```python
x = np.arange(len(species))
width = 0.25
multiplier = 0

fig, ax = plt.subplots()

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    multiplier += 1
```
