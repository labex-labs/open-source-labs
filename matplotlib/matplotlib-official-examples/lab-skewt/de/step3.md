# Definieren der SkewXAxis-Klasse

Die SkewXAxis-Klasse wird verwendet, um zwei separate Sets von Intervallen für die Markierungen bereitzustellen und Instanzen der benutzerdefinierten Markierung zu erstellen.

```python
class SkewXAxis(maxis.XAxis):
    def _get_tick(self, major):
        return SkewXTick(self.axes, None, major=major)

    def get_view_interval(self):
        return self.axes.upper_xlim[0], self.axes.lower_xlim[1]
```
