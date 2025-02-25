# Anpassen des Diagramms

Wir können das Diagramm anpassen, indem wir die Grundlinie mit dem Parameter `bottom` anpassen. Wir können auch die Format-Eigenschaften des Diagramms mit den Parametern `linefmt`, `markerfmt` und `basefmt` anpassen.

```python
markerline, stemlines, baseline = plt.stem(
    x, y, linefmt='grey', markerfmt='D', bottom=1.1)
markerline.set_markerfacecolor('none')
plt.show()
```

Dies erzeugt ein Diagramm mit einem grauen Linienformat und diamantförmigen Markern. Die Grundlinie wurde auch auf 1.1 eingestellt.
