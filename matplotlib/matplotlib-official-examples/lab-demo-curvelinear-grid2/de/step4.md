# Definieren von Achsen und Anzeigen eines Bildes

Der vierte Schritt besteht darin, die Achsen mithilfe der in Schritt 3 erstellten `grid_helper`-Instanz zu definieren. Wir werden auch ein Bild mit der `imshow`-Funktion anzeigen.

```python
ax1 = fig.add_subplot(axes_class=Axes, grid_helper=grid_helper)
ax1.imshow(np.arange(25).reshape(5, 5), vmax=50, cmap=plt.cm.gray_r, origin="lower")
```
