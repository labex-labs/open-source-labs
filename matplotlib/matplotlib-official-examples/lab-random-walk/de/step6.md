# Erstellen einer Animation

Wir erstellen eine Animation mit der Klasse `FuncAnimation` aus `matplotlib.animation`. Wir übergeben das Figure-Objekt, die Update-Funktion, die Gesamtzahl der Frames (die der Anzahl der Schritte in den Zufallswalks entspricht), die Liste aller Zufallswalks und die Liste aller Linien als Argumente an den `FuncAnimation`-Konstruktor.

```python
# Creating the Animation object
ani = animation.FuncAnimation(
    fig, update_lines, num_steps, fargs=(walks, lines), interval=100)
```
