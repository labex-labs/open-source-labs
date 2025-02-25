# Füge einen Polygon-Pfad mit Schraffierung hinzu

Du kannst auch einen Polygon-Pfad mit Schraffierung hinzufügen. In diesem Fall werden wir die `add_patch`-Funktion verwenden, um einen Polygon-Pfad zu unserem Diagramm hinzuzufügen.

```python
plt.gca().add_patch(Polygon([(10, 20), (30, 50), (50, 10)], hatch='\\/...', facecolor='g'))
```
