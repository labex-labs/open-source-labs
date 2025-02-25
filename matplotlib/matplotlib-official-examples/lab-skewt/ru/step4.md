# Определяем класс SkewSpine

Класс SkewSpine вычисляет отдельный диапазон данных для верхней оси X и рисует спинну (ребро) там. Он также предоставляет этот диапазон художнику оси X для делений и сеток.

```python
class SkewSpine(mspines.Spine):
    def _adjust_location(self):
        pts = self._path.vertices
        if self.spine_type == 'top':
            pts[:, 0] = self.axes.upper_xlim
        else:
            pts[:, 0] = self.axes.lower_xlim
```
