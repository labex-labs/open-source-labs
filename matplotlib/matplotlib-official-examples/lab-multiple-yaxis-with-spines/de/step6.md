# Festlegen der Grenzen und Beschriftungen der Achsen

Wir legen die Grenzen und Beschriftungen für jede y-Achse mit der `set`-Methode fest. Wir setzen auch die Farbe der Beschriftungen, um sie der Farbe der Linien zu entsprechen, indem wir die `set_color`-Methode verwenden.

```python
ax.set(xlim=(0, 2), ylim=(0, 2), xlabel="Distance", ylabel="Density")
twin1.set(ylim=(0, 4), ylabel="Temperature")
twin2.set(ylim=(1, 65), ylabel="Velocity")

ax.yaxis.label.set_color(p1.get_color())
twin1.yaxis.label.set_color(p2.get_color())
twin2.yaxis.label.set_color(p3.get_color())
```
