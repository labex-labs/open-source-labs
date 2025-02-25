# Vertikale Linie hinzufügen

Fügen Sie vertikale Linien hinzu, indem Sie die `axvline()`-Funktion verwenden.

```python
# Vertikale Linie bei x=1, die den gesamten y-Bereich abdeckt.
ax.axvline(x=1)
# Dicke blaue vertikale Linie bei x=0, die den oberen Viertel des y-Bereichs abdeckt.
ax.axvline(x=0, ymin=0.75, linewidth=8, color='#1f77b4')
```
