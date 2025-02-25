# Füge eine Legende und Achsenfarben hinzu

Wir fügen einer Legende zu den Hauptachsen mit der `host.legend()`-Methode hinzu. Wir setzen auch die Farbe der linken y-Achsenbezeichnung der Hauptachsen, der rechten y-Achsenbezeichnung der ersten Parasitenachse und der rechten y-Achsenbezeichnung der zweiten Parasitenachse, um sie mit ihren jeweiligen Linien zu koordinieren, mit den Methoden `host.axis["left"].label.set_color(p1.get_color())`, `par1.axis["right"].label.set_color(p2.get_color())` und `par2.axis["right2"].label.set_color(p3.get_color())`.

```python
host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right2"].label.set_color(p3.get_color())
```
