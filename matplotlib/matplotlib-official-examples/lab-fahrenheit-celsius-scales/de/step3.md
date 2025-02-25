# Definieren einer Funktion zum Aktualisieren der zweiten Achse

Wir werden eine Closure-Funktion definieren, um uns als Callback zu registrieren, um die zweite Achse gemäß der ersten Achse zu aktualisieren.

```python
def convert_ax_c_to_celsius(ax_f):
    """
    Aktualisiere die zweite Achse gemäß der ersten Achse.
    """
    y1, y2 = ax_f.get_ylim()
    ax_c.set_ylim(fahrenheit2celsius(y1), fahrenheit2celsius(y2))
    ax_c.figure.canvas.draw()
```
