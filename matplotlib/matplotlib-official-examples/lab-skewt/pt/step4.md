# Definir a Classe SkewSpine

A classe SkewSpine calcula a faixa de dados separada do eixo X superior e desenha a espinha (spine) ali. Ela também fornece essa faixa ao artista do eixo X para ticks e linhas de grade.

```python
class SkewSpine(mspines.Spine):
    def _adjust_location(self):
        pts = self._path.vertices
        if self.spine_type == 'top':
            pts[:, 0] = self.axes.upper_xlim
        else:
            pts[:, 0] = self.axes.lower_xlim
```
