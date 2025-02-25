# Erstellen des 3D-Diagramms

Wir verwenden `subplot_mosaic`, um das 3D-Diagramm basierend auf dem im Schritt 4 definierten Layout zu erstellen.

```python
fig, axd = plt.subplot_mosaic(layout, subplot_kw={'projection': '3d'},
                              figsize=(12, 8.5))
```
