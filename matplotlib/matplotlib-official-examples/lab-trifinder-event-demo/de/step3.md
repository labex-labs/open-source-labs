# Diagramm einrichten

Jetzt können wir das Diagramm einrichten. Wir werden `plt.subplots()` verwenden, um eine Figur und ein Achsenobjekt zu erstellen. Anschließend werden wir `ax.triplot()` verwenden, um die Triangulation zu zeichnen.

```python
fig, ax = plt.subplots()
ax.triplot(triang)
```
