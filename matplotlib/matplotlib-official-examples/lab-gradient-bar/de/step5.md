# Erstellen des Diagramms

Jetzt können wir das Diagramm erstellen. Wir werden zunächst eine Figur und ein Achsenobjekt erstellen. Anschließend werden wir die x- und y-Bereiche der Achsen festlegen. Wir werden einen Gradientenhintergrund mit der Funktion `gradient_image()` erstellen. Schließlich werden wir einen zufälligen Datensatz erstellen und die Funktion `gradient_bar()` verwenden, um das Balkendiagramm zu erstellen.

```python
fig, ax = plt.subplots()
ax.set(xlim=(0, 10), ylim=(0, 1))

# Hintergrundbild
gradient_image(ax, direction=1, extent=(0, 1, 0, 1), transform=ax.transAxes,
               cmap=plt.cm.RdYlGn, cmap_range=(0.2, 0.8), alpha=0.5)

N = 10
x = np.arange(N) + 0.15
y = np.random.rand(N)
gradient_bar(ax, x, y, width=0.7)
plt.show()
```
