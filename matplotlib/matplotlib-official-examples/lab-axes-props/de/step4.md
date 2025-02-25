# Achsenmarkierungen und Gittereigenschaften anpassen

Wir können die Achsenmarkierungen und die Gittereigenschaften mit den Funktionen `grid()` und `tick_params()` anpassen. In diesem Beispiel werden wir die Farbe und Größe der Markierungsbeschriftungen sowie die Breite und den Stil der Gitterlinien ändern.

```python
ax.grid(True, linestyle='-.', linewidth=0.5, color='gray')
ax.tick_params(axis='both', which='both', labelsize=8, width=1, color='red')
```
