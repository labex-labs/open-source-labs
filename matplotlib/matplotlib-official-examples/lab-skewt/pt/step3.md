# Definir a Classe SkewXAxis

A classe SkewXAxis é usada para fornecer dois conjuntos separados de intervalos ao tick e criar instâncias do tick personalizado.

```python
class SkewXAxis(maxis.XAxis):
    def _get_tick(self, major):
        return SkewXTick(self.axes, None, major=major)

    def get_view_interval(self):
        return self.axes.upper_xlim[0], self.axes.lower_xlim[1]
```
