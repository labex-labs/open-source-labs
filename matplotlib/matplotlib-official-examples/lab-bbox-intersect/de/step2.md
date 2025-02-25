# Einrichten des Rechtecks

Wir werden die Position und die Maße des Rechtecks mithilfe der Variablen `left`, `bottom`, `width` und `height` definieren. Anschließend werden wir das Rechteck mithilfe der `Rectangle`-Klasse erstellen und es mit der `add_patch`-Methode zum Graphen hinzufügen.

```python
left, bottom, width, height = (-1, -1, 2, 2)
rect = plt.Rectangle((left, bottom), width, height,
                     facecolor="black", alpha=0.1)

fig, ax = plt.subplots()
ax.add_patch(rect)
```
