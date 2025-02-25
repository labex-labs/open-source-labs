# Erstellen der Animation

Der letzte Schritt ist es, die Animation zu erstellen. Wir tun dies mithilfe der FuncAnimation-Funktion aus dem animation-Modul. Diese Funktion nimmt einige Argumente entgegen, darunter das Figure-Objekt, die Funktion, die das Diagramm aktualisiert, und die Anzahl der Frames, die verwendet werden sollen.

```python
def animate(i):
    scat.set_offsets((x[i], 0))
    return scat,

ani = animation.FuncAnimation(fig, animate, repeat=True,
                                    frames=len(x) - 1, interval=50)
```
