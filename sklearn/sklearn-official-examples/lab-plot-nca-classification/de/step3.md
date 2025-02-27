# Farbskalen erstellen

Wir werden nun Farbskalen erstellen, um die Klassifizierungsgrenzen zu plotten. Wir werden helle Farben für den Hintergrund und fette Farben für die Klassenfarben verwenden.

```python
h = 0.05  # Schrittweite im Gitter

# Farbskalen erstellen
cmap_light = ListedColormap(["#FFAAAA", "#AAFFAA", "#AAAAFF"])
cmap_bold = ListedColormap(["#FF0000", "#00FF00", "#0000FF"])
```
