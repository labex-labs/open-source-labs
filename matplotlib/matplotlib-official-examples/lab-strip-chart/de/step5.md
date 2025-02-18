# Das Diagramm einrichten

Wir erstellen ein neues Diagramm (Figure) und ein Achsenobjekt (Axis) und initialisieren die `Scope`-Klasse. Anschließend übergeben wir die `update`- und `emitter`-Funktionen an die `FuncAnimation`-Methode, um die Animation zu erstellen.

```python
fig, ax = plt.subplots()
scope = Scope(ax)

ani = animation.FuncAnimation(fig, scope.update, emitter, interval=50,
                              blit=True, save_count=100)

plt.show()
```
