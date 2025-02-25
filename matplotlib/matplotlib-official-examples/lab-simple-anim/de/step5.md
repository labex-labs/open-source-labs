# Das Animationsobjekt erstellen

Jetzt können wir das Animationsobjekt mit der Funktion `FuncAnimation()` erstellen. Wir werden das Figurobjekt, die Animationsfunktion, das Aktualisierungsintervall und die Anzahl der zu speichernden Frames übergeben.

```python
ani = animation.FuncAnimation(
    fig, animate, interval=20, blit=True, save_count=50)
```
