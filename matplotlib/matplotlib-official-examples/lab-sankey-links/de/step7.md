# Fügen des ersten Diagramms hinzu

Wir fügen das erste Diagramm hinzu, indem wir `sankey.add()` mit `flows=[1, -1]` und `orientations=[0, 1]` verwenden.

```python
sankey.add(flows=[1, -1], orientations=[0, 1],
           patchlabel="0", facecolor='k',
           rotation=45)
```
