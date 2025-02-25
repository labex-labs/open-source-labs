# Rechteck hinzufügen

Fügen Sie ein Rechteck hinzu, indem Sie die `axhspan()`- und `axvspan()`-Funktionen verwenden.

```python
# 50%-graues Rechteck, das die Breite der Achsen von y=0,25 bis y=0,75 abdeckt.
ax.axhspan(0.25, 0.75, facecolor='0.5')
# Grünes Rechteck, das die Höhe der Achsen von x=1,25 bis x=1,55 abdeckt.
ax.axvspan(1.25, 1.55, facecolor='#2ca02c')
```
