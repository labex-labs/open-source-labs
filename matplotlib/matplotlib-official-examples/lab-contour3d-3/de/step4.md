# Projektieren von Konturprofilen auf die Wände des Graphen

In diesem Schritt werden wir Konturprofile auf die Wände des Graphen projizieren, indem wir die Konturen für jede Dimension mit geeigneten Verschiebungen zeichnen.

```python
# Zeichnen von Projektionen der Konturen für jede Dimension
ax.contour(X, Y, Z, zdir='z', offset=-100, cmap='coolwarm')
ax.contour(X, Y, Z, zdir='x', offset=-40, cmap='coolwarm')
ax.contour(X, Y, Z, zdir='y', offset=40, cmap='coolwarm')
```
