# Die Animation erstellen

Der siebte Schritt besteht darin, das Animationsobjekt mit der `FuncAnimation`-Funktion zu erstellen. Wir übergeben das Figure-Objekt, die Animationsfunktion, den Zeitintervall zwischen den Frames in Millisekunden, die Anzahl der Frames und eine Verzögerung vor dem Wiederholen der Animation.

```python
ani = animation.FuncAnimation(
    fig,
    animate,
    interval=50,
    blit=False,  # blitting kann nicht mit Figure-Künstlern verwendet werden
    frames=x,
    repeat_delay=100,
)
```
