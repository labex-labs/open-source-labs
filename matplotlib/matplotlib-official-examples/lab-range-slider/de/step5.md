# Erstelle eine Callback-Funktion für den Slider

Wir werden eine Callback-Funktion erstellen, die jedes Mal aufgerufen wird, wenn der Benutzer die Schwellwerte mit dem Slider ändert. Die Funktion wird die Farbkarte des Bildes und die Positionen der vertikalen Linien auf dem Histogramm aktualisieren.

```python
def update(val):
    # Der Wert, der an eine Callback-Funktion von RangeSlider übergeben wird,
    # wird ein Tupel von (min, max) sein

    # Aktualisiere die Farbkarte des Bildes
    im.norm.vmin = val[0]
    im.norm.vmax = val[1]

    # Aktualisiere die Position der vertikalen Linien
    lower_limit_line.set_xdata([val[0], val[0]])
    upper_limit_line.set_xdata([val[1], val[1]])

    # Zeichne die Figur erneut, um sicherzustellen, dass sie aktualisiert wird
    fig.canvas.draw_idle()


slider.on_changed(update)
```
