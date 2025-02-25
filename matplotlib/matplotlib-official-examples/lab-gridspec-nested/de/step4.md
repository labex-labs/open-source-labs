# Teilplots zum inneren GridSpec hinzufügen

Wir werden nun Teilplots zum inneren GridSpec hinzufügen. Wir werden drei Teilplots erstellen: `ax1`, `ax2` und `ax3`.

```python
ax1 = fig.add_subplot(gs00[:-1, :])
ax2 = fig.add_subplot(gs00[-1, :-1])
ax3 = fig.add_subplot(gs00[-1, -1])
```
