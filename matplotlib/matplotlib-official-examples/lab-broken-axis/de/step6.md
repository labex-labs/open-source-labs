# Verstecken der Achsenlinien (Spines)

Wir werden nun die Achsenlinien zwischen den beiden Teilplots (Subplots) verstecken, indem wir `ax1.spines.bottom.set_visible` und `ax2.spines.top.set_visible` verwenden.

```python
ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)
```
