# Definir la clase SkewXAxis

La clase SkewXAxis se utiliza para proporcionar dos conjuntos separados de intervalos a la marca de graduación y crear instancias de la marca de graduación personalizada.

```python
class SkewXAxis(maxis.XAxis):
    def _get_tick(self, major):
        return SkewXTick(self.axes, None, major=major)

    def get_view_interval(self):
        return self.axes.upper_xlim[0], self.axes.lower_xlim[1]
```
