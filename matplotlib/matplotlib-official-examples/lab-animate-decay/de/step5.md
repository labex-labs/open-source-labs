# Die Animationsfunktion definieren

Jetzt müssen wir die Funktion definieren, die das Diagramm für jedes Frame der Animation aktualisiert. Diese Funktion wird die von der `data_gen()`-Funktion generierten Daten entgegennehmen und das Diagramm mit den neuen Daten aktualisieren. Wir werden auch die X-Achsengrenzen aktualisieren, während die Animation abläuft.

```python
def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,
```
