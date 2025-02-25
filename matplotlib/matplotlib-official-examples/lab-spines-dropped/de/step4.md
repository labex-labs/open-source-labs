# Die Achsenlinien verschieben

Wir verschieben die linke und untere Achsenlinie um 10 Punkte nach außen mit der `set_position()`-Funktion. Der Argumentwert für `set_position()` ist ein Tupel mit zwei Elementen. Das erste Element stellt die Position der Achsenlinie dar, und das zweite Element die Entfernung von der Achsenlinie zum Diagrammbereich.

```python
ax.spines[['left', 'bottom']].set_position(('outward', 10))
```
