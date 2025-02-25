# Erstellen von gefüllten Konturen mit Löchern

Mehrere gefüllte Konturlinien können in einer einzelnen Liste von Polygon-Eckenpunkte zusammen mit einer Liste von Eckpunkt-Arten (Codetypen) wie in der Path-Klasse beschrieben angegeben werden. Dies ist besonders nützlich für Polygone mit Löchern.

```python
fig, ax = plt.subplots()
filled01 = [[[0, 0], [3, 0], [3, 3], [0, 3], [1, 1], [1, 2], [2, 2], [2, 1]]]
M = Path.MOVETO
L = Path.LINETO
kinds01 = [[M, L, L, L, M, L, L, L]]
cs = ContourSet(ax, [0, 1], [filled01], [kinds01], filled=True)
cbar = fig.colorbar(cs)

ax.set(xlim=(-0.5, 3.5), ylim=(-0.5, 3.5),
       title='User specified filled contours with holes')
```
