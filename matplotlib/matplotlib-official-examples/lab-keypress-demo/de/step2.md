# Definiere die Tastendruck-Ereignisfunktion

Als nächstes definieren wir eine Funktion `on_press`, die aufgerufen wird, wenn eine Taste gedrückt wird. Diese Funktion nimmt einen `event`-Parameter entgegen, der Informationen über die gedrückte Taste enthält. In diesem Beispiel werden wir die Sichtbarkeit der x-Achsebeschriftung umschalten, wenn die Taste 'x' gedrückt wird.

```python
def on_press(event):
    print('press', event.key)
    sys.stdout.flush()
    if event.key == 'x':
        visible = xl.get_visible()
        xl.set_visible(not visible)
        fig.canvas.draw()
```
