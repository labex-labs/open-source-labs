# Vorbereiten der Koordinaten

Als Nächstes werden wir die Koordinaten für unseren Voxelplot vorbereiten. Wir werden ein 8x8x8-Gitter von Punkten mithilfe der Funktion `indices` von NumPy erstellen.

```python
x, y, z = np.indices((8, 8, 8))
```
