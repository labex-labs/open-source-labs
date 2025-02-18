# Anpassen der Tick-Marken (Teilstriche)

Wir werden nun die Tick-Marken auf der x-Achse anpassen. Wir verschieben die Tick-Marken des ersten Teilplots (Subplots) nach oben mithilfe von `ax1.xaxis.tick_top`, entfernen die Tick-Beschriftungen des ersten Teilplots mit `ax1.tick_params(labeltop=False)` und behalten die Tick-Beschriftungen des zweiten Teilplots bei.

```python
ax1.xaxis.tick_top()
ax1.tick_params(labeltop=False)
ax2.xaxis.tick_bottom()
```
