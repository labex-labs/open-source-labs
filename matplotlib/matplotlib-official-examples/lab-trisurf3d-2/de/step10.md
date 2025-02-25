# Zeichnen der Fläche

Schließlich zeichnen wir die Fläche mit der Funktion `plot_trisurf()`.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(triang, z, cmap=plt.cm.CMRmap)
```
