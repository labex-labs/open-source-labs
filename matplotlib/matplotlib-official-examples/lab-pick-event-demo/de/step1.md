# Einfaches Auswählen, Linien, Rechtecke und Text

Wir beginnen, indem wir das einfache Auswählen aktivieren, indem wir die Eigenschaft "picker" eines Künstlers festlegen. Dadurch wird es dem Künstler ermöglicht, ein Auswählevent auszulösen, wenn das Mausereignis über dem Künstler liegt. Wir werden ein einfaches Diagramm erstellen, das eine Linie, ein Rechteck und Text enthält, und das Auswählen für jeden dieser Künstler aktivieren.

```python
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.set_title('click on points, rectangles or text', picker=True)
ax1.set_ylabel('ylabel', picker=True, bbox=dict(facecolor='red'))
line, = ax1.plot(rand(100), 'o', picker=True, pickradius=5)

# Wählen Sie das Rechteck aus.
ax2.bar(range(10), rand(10), picker=True)
for label in ax2.get_xticklabels():  # Machen Sie die xtick-Labels wählbar.
    label.set_picker(True)
```
