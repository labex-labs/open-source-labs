# Spines mit Grenzen, die auf den Datenbereich beschränkt sind, anpassen

Im dritten Subplot werden wir Spines mit Grenzen anzeigen, die auf den Datenbereich beschränkt sind. Wir können die Ausdehnung jeder Spine auf den Datenbereich begrenzen, indem wir die `set_bounds`-Methode verwenden.

```python
ax2.plot(x, y)
ax2.set_title('Spines with Bounds Limited to Data Range')

# Only draw spines for the data range, not in the margins
ax2.spines.bottom.set_bounds(x.min(), x.max())
ax2.spines.left.set_bounds(y.min(), y.max())
# Hide the right and top spines
ax2.spines.right.set_visible(False)
ax2.spines.top.set_visible(False)
```
