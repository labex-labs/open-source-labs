# Definieren der SkewSpine-Klasse

Die SkewSpine-Klasse berechnet den separaten Datenbereich der oberen X-Achse und zeichnet dort die Spur. Sie liefert auch diesen Bereich an den X-Achsen-Künstler für die Markierungen und die Rasterlinien.

```python
class SkewSpine(mspines.Spine):
    def _adjust_location(self):
        pts = self._path.vertices
        if self.spine_type == 'top':
            pts[:, 0] = self.axes.upper_xlim
        else:
            pts[:, 0] = self.axes.lower_xlim
```
