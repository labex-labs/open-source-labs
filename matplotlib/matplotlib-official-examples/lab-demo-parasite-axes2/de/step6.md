# Legende und Farbe hinzufügen

Wir werden einer Grafik eine Legende hinzufügen und die Beschriftungen jeder Achse in die Farbe des entsprechenden Datensatzes einfärben, indem wir die Funktionen `legend()` und `label.set_color()` verwenden.

```python
host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right"].label.set_color(p3.get_color())
```
