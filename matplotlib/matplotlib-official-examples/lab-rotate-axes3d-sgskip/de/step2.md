# Erstellen eines 3D-Graphen

Als nächstes werden wir einen 3D-Graphen mit den Funktionen `plt.figure()` und `fig.add_subplot()` erstellen. Wir werden auch die Funktion `ax.plot_wireframe()` verwenden, um den Datensatz als Drahtgitter zu plotten.

```python
# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Plot wireframe
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```
