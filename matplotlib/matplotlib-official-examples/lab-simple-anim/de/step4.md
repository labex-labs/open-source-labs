# Die Animationsfunktion definieren

Die Animationsfunktion wird von der Funktion `FuncAnimation()` aufgerufen und wird verwendet, um das Diagramm mit neuen Daten zu aktualisieren. In diesem Beispiel werden wir die y-Achsenwerte des Liniendiagramms mit einer Sinuswelle aktualisieren, die über die Zeit eine sich ändernde Amplitude hat.

```python
def animate(i):
    line.set_ydata(np.sin(x + i / 50))  # update the data.
    return line,
```
