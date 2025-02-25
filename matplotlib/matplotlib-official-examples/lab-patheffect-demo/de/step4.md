# Schatten-Effekt zur Legende hinzufügen

Wir können einen Schatten-Effekt zu einer Legende hinzufügen, indem wir den `withSimplePatchShadow`-Pfadeffekt verwenden.

```python
# Create plot and add shadow effect to legend
fig, ax = plt.subplots()
p1, = ax.plot([0, 1], [0, 1])
leg = ax.legend([p1], ["Line 1"], fancybox=True, loc='upper left')
leg.legendPatch.set_path_effects([patheffects.withSimplePatchShadow()])

plt.show()
```
