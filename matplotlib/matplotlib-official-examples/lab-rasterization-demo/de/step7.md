# Ein pcolormesh-Diagramm mit einem überlagerten Text mit Rasterisierung erstellen

Wir werden ein pcolormesh-Diagramm mit einem überlagerten Text mit Rasterisierung erstellen, um zu veranschaulichen, wie die Rasterisierung es Vektorgrafiken ermöglicht, die Vorteile von Vektorgrafiken für einige Künstler wie die Achsen und den Text beizubehalten.

```python
ax4.set_aspect(1)
m = ax4.pcolormesh(xx, yy, d, zorder=-10)
ax4.text(0.5, 0.5, "Text", alpha=0.2,
         va="center", ha="center", size=50, transform=ax4.transAxes)
ax4.set_rasterization_zorder(0)
ax4.set_title("Rasterization z$<-10$")
```
