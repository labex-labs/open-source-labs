# Das Diagramm erstellen

Jetzt, wo wir unsere Daten haben, können wir das Gittersdiagramm erstellen. In diesem Beispiel werden wir die Funktion `plot_wireframe()` verwenden, um das Diagramm zu erstellen.

```python
# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)
```
