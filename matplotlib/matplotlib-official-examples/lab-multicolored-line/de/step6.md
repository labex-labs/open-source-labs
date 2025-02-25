# Verwenden einer Boundary Norm

Wir werden stattdessen eine Boundary Norm verwenden, um die Liniensegmente zu färben. Wir werden eine `ListedColormap` erstellen, die drei Farben enthält: rot, grün und blau. Anschließend werden wir eine `BoundaryNorm` mit den Grenzen -1, -0,5, 0,5 und 1 und der `ListedColormap` erstellen. Wir werden die `set_array`-Funktion verwenden, um die Werte festzulegen, die für die Farbzuordnung verwendet werden.

```python
cmap = ListedColormap(['r', 'g', 'b'])
norm = BoundaryNorm([-1, -0.5, 0.5, 1], cmap.N)
lc = LineCollection(segments, cmap=cmap, norm=norm)
lc.set_array(dydx)
lc.set_linewidth(2)
```
