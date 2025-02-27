# Erstellen eines pcolormesh-Plots mit einem überlagerten Text mit Ver光栅isierung

Wir werden einen pcolormesh-Plot mit einem überlagerten Text mit Ver光栅isierung erstellen, um zu veranschaulichen, wie die Ver光栅isierung es Vektorgrafiken ermöglicht, die Vorteile von Vektorgrafiken für einige Künstler wie Achsen und Text beizubehalten.

```python
ax4.set_aspect(1)
m = ax4.pcolormesh(xx, yy, d, zorder=-10)
ax4.text(0.5, 0.5, "Text", alpha=0.2,
         va="center", ha="center", size=50, transform=ax4.transAxes)
ax4.set_rasterization_zorder(0)
ax4.set_title("Ver光栅isierung z$<-10$")
```