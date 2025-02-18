# Die Scope-Klasse einrichten

Die `Scope`-Klasse wird die Daten und Methoden enthalten, die wir für die Erstellung des Oszilloskops benötigen. Im Konstruktor initialisieren wir die erforderlichen Variablen und richten das Diagramm ein.

```python
class Scope:
    def __init__(self, ax, maxt=2, dt=0.02):
        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = [0]
        self.ydata = [0]
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(-.1, 1.1)
        self.ax.set_xlim(0, self.maxt)
```
