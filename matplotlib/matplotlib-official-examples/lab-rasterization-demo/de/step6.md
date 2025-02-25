# Erstellen eines pcolormesh-Diagramms mit einem überlagerten Text ohne Ver光栅isierung

Wir werden ein pcolormesh-Diagramm mit einem überlagerten Text ohne Ver光栅isierung erstellen, um zu veranschaulichen, wie Vektorgrafiken die Vorteile von Vektorgrafiken für einige Künstler wie Achsen und Text beibehalten können.

```python
ax3.set_aspect(1)
ax3.pcolormesh(xx, yy, d)
ax3.text(0.5, 0.5, "Text", alpha=0.2,
         va="center", ha="center", size=50, transform=ax3.transAxes)
ax3.set_title("No Rasterization")
```
