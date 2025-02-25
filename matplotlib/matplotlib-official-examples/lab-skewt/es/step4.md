# Definir la clase SkewSpine

La clase SkewSpine calcula el rango de datos separado del eje X superior y dibuja la espina allí. También proporciona este rango al artista del eje X para la marcas de graduación y las líneas de cuadrícula.

```python
class SkewSpine(mspines.Spine):
    def _adjust_location(self):
        pts = self._path.vertices
        if self.spine_type == 'top':
            pts[:, 0] = self.axes.upper_xlim
        else:
            pts[:, 0] = self.axes.lower_xlim
```
