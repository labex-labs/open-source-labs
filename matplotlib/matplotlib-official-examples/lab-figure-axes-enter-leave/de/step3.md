# Definieren der Ereignishandler

Wir werden jetzt vier Ereignishandlerfunktionen definieren: `on_enter_axes`, `on_leave_axes`, `on_enter_figure` und `on_leave_figure`. Diese Funktionen werden aufgerufen, wenn die Maus in eine Achse oder die Figur eintritt oder verlässt.

```python
def on_enter_axes(event):
    print('enter_axes', event.inaxes)
    event.inaxes.patch.set_facecolor('yellow')
    event.canvas.draw()

def on_leave_axes(event):
    print('leave_axes', event.inaxes)
    event.inaxes.patch.set_facecolor('white')
    event.canvas.draw()

def on_enter_figure(event):
    print('enter_figure', event.canvas.figure)
    event.canvas.figure.patch.set_facecolor('red')
    event.canvas.draw()

def on_leave_figure(event):
    print('leave_figure', event.canvas.figure)
    event.canvas.figure.patch.set_facecolor('grey')
    event.canvas.draw()
```
