# Dessiner des flèches à la fin des axes (spines)

Pour indiquer la direction des axes, vous pouvez dessiner des flèches à la fin des axes (spines).

```python
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
```
