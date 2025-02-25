# Callback-Funktion definieren

Wir müssen eine Callback-Funktion für die Checkbuttons definieren. Diese Funktion wird jedes Mal aufgerufen, wenn eine Checkbox angeklickt wird. Wir werden diese Funktion verwenden, um die Sichtbarkeit der entsprechenden Linie im Plot umzuschalten.

```python
def callback(label):
    ln = lines_by_label[label]
    ln.set_visible(not ln.get_visible())
    ln.figure.canvas.draw_idle()

check.on_clicked(callback)
```
