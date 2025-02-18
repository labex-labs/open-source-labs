# Festlegen der Farben

Jetzt werden wir die Farben für jedes Objekt im Voxelplot festlegen. Dazu erstellen wir ein leeres Array in der gleichen Form wie das boolesche Array, das wir in Schritt 3 erstellt haben, und setzen dann die Farbe jedes Objekts basierend auf seiner Position.

```python
colors = np.empty(voxelarray.shape, dtype=object)
colors[link] = 'red'
colors[cube1] = 'blue'
colors[cube2] = 'green'
```
