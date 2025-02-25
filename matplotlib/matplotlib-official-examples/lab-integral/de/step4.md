# Erzeuge das Diagramm

Erzeugen Sie ein Figure- und Achsenobjekt mit `subplots`. Plotten Sie die x- und y-Werte mit `plot`. Setzen Sie die untere Grenze der y-Achse auf 0 mit `set_ylim`.

```python
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.set_ylim(bottom=0)
```
