# Die Initialisierungsfunktion definieren

Wir müssen eine Initialisierungsfunktion definieren, die den Anfangszustand des Diagramms festlegt. In dieser Funktion werden wir die Y-Achsengrenzen festlegen und die Daten aus dem Linienobjekt löschen.

```python
def init():
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 1)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,
```
