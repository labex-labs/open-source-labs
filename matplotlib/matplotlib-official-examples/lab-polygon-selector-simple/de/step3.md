# Interaktives Erstellen eines Polygons

Um ein Polygon interaktiv zu erstellen, müssen wir ein `Figure`-Objekt und ein `Axes`-Objekt erstellen. Anschließend können wir ein `PolygonSelector`-Objekt erstellen und ihm durch Klicken auf das Diagramm Eckpunkte hinzufügen. Wir können auch die `Shift`- und `Ctrl`-Tasten verwenden, um die Eckpunkte zu bewegen.

```python
fig, ax = plt.subplots()
selector = PolygonSelector(ax, lambda *args: None)

print("Klicken Sie auf die Figur, um ein Polygon zu erstellen.")
print("Drücken Sie die 'Esc'-Taste, um ein neues Polygon zu starten.")
print("Versuchen Sie, die 'Shift'-Taste gedrückt zu halten, um alle Eckpunkte zu bewegen.")
print("Versuchen Sie, die 'Ctrl'-Taste gedrückt zu halten, um einen einzelnen Eckpunkt zu bewegen.")

plt.show()
```
