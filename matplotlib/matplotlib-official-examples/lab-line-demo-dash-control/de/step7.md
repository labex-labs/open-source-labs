# Andere Attribute des Strichs mit relevanten Methoden einstellen

Andere Attribute des Strichs können auch mit relevanten Methoden wie `~.Line2D.set_dash_joinstyle()`, `~.Line2D.set_dash_joinstyle()` und `~.Line2D.set_gapcolor()` eingestellt werden. In diesem Beispiel werden wir die Parameter `dashes` und `gapcolor` verwenden, um die Strichfolge und den alternierenden Farbverlauf für `line3` festzulegen.

```python
line3, = ax.plot(x, y - 0.4, dashes=[4, 4], gapcolor='tab:pink',
                 label='Using the dashes and gapcolor parameters')
```
