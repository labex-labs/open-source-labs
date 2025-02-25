# Die Animationsfunktion definieren

Der sechste Schritt besteht darin, die Animationsfunktion zu definieren. Diese Funktion wird für jedes Frame der Animation aufgerufen und aktualisiert die Position des Punktes auf dem linken Teilplot, die Position und die Daten der Sinuskurve auf dem rechten Teilplot sowie die Position des Verbindungspatches.

```python
def animate(i):
    x = np.linspace(0, i, int(i * 25 / np.pi))
    sine.set_data(x, np.sin(x))
    x, y = np.cos(i), np.sin(i)
    point.set_data([x], [y])
    con.xy1 = x, y
    con.xy2 = i, y
    return point, sine, con
```
