# Timer-Objekt erstellen

Erstellen Sie ein neues Timer-Objekt. Legen Sie das Intervall auf 100 Millisekunden fest (Standardwert ist 1000) und geben Sie an, welche Funktion vom Timer aufgerufen werden soll.

```python
timer = fig.canvas.new_timer(interval=100)
timer.add_callback(update_title, ax)
```
