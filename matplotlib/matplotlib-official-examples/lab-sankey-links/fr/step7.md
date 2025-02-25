# Ajouter le premier diagramme

Nous ajoutons le premier diagramme à l'aide de `sankey.add()` avec `flows=[1, -1]` et `orientations=[0, 1]`.

```python
sankey.add(flows=[1, -1], orientations=[0, 1],
           patchlabel="0", facecolor='k',
           rotation=45)
```
