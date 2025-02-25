# Définir la classe SkewXAxis

La classe SkewXAxis est utilisée pour fournir deux ensembles distincts d'intervalles aux graduations et créer des instances de la graduation personnalisée.

```python
class SkewXAxis(maxis.XAxis):
    def _get_tick(self, major):
        return SkewXTick(self.axes, None, major=major)

    def get_view_interval(self):
        return self.axes.upper_xlim[0], self.axes.lower_xlim[1]
```
