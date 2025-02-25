# Zeichnen von Linien

Wir zeichnen zwei Linien mit `ax.plot()`. Wir passen auch die Linien mit unterschiedlichen Farben, Markern und Beschriftungen an.

```python
l1, = ax.plot([0.1, 0.5, 0.9], [0.1, 0.9, 0.5], "bo-", mec="b", lw=5, ms=10, label="Line 1")
l2, = ax.plot([0.1, 0.5, 0.9], [0.5, 0.2, 0.7], "rs-", mec="r", lw=5, ms=10, label="Line 2")
```
