# Teilplots zum zweiten inneren GridSpec hinzufügen

Wir werden nun Teilplots zum zweiten inneren GridSpec hinzufügen. Wir werden drei Teilplots erstellen: `ax4`, `ax5` und `ax6`.

```python
ax4 = fig.add_subplot(gs01[:, :-1])
ax5 = fig.add_subplot(gs01[:-1, -1])
ax6 = fig.add_subplot(gs01[-1, -1])
```
