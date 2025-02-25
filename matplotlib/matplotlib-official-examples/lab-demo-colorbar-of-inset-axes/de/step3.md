# Ein eingebettetes Achsenbereich erstellen

Erstelle einen eingebetteten Achsenbereich mit der Funktion `zoomed_inset_axes`. Setze das Zoomlevel und den Ort des eingebetteten Achsenbereichs innerhalb des Hauptplots.

```python
axins = zoomed_inset_axes(ax, zoom=2, loc='upper left')
axins.set(xticks=[], yticks=[])
```
