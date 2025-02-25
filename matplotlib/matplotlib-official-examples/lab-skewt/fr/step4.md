# Définir la classe SkewSpine

La classe SkewSpine calcule la plage de données séparée de l'axe X supérieur et dessine l'arête à cet emplacement. Elle fournit également cette plage à l'artiste de l'axe X pour les graduations et les lignes de grille.

```python
class SkewSpine(mspines.Spine):
    def _adjust_location(self):
        pts = self._path.vertices
        if self.spine_type == 'top':
            pts[:, 0] = self.axes.upper_xlim
        else:
            pts[:, 0] = self.axes.lower_xlim
```
