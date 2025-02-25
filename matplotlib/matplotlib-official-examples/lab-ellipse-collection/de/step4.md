# Die Farbe der Ellipsen festlegen

Wir legen die Farbe jeder Ellipse in der `EllipseCollection` basierend auf der Summe ihrer x- und y-Koordinaten fest.

```python
ec.set_array((X + Y).ravel())
```
