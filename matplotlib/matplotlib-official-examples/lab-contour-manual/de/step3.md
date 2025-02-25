# Erstellen des Diagramms

Der nächste Schritt besteht darin, das Diagramm zu erstellen. Dies kann mit der ContourSet-Funktion durchgeführt werden.

```python
fig, ax = plt.subplots()

# Gefüllte Konturen mit filled=True.
cs = ContourSet(ax, [0, 1, 2], [filled01, filled12], filled=True, cmap=cm.bone)
cbar = fig.colorbar(cs)

# Konturlinien (nicht gefüllt).
lines = ContourSet(
    ax, [0, 1, 2], [lines0, lines1, lines2], cmap=cm.cool, linewidths=3)
cbar.add_lines(lines)

ax.set(xlim=(-0.5, 3.5), ylim=(-0.5, 4.5),
       title='User-specified contours')
```
