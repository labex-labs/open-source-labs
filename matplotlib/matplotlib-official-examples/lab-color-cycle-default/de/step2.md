# Definieren des Eigenschaftenzyklus und Abrufen von Farben

Als nächstes müssen wir den Eigenschaftenzyklus definieren und die darin enthaltenen Farben abrufen.

```python
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']
```
