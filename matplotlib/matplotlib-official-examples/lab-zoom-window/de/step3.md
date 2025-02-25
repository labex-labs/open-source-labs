# Verbinden des Ereignisses mit der Funktion

Jetzt verbinden wir das Ereignis eines Mausklicks im ersten Fenster mit der zuvor definierten on_press-Funktion.

```python
figsrc.canvas.mpl_connect('button_press_event', on_press)
```
