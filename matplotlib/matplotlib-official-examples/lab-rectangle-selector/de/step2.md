# Definieren der Auswahlrückruffunktion

Die Auswahlrückruffunktion wird jedes Mal aufgerufen, wenn der Benutzer ein Rechteck oder eine Ellipse auswählt. Die Funktion erhält die Klick- und Loslassereignisse als Argumente und druckt die Koordinaten des Rechtecks oder der Ellipse aus.

```python
def select_callback(eclick, erelease):
    """
    Callback für die Linienauswahl.

    *eclick* und *erelease* sind die Drück- und Loslassereignisse.
    """
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    print(f"({x1:3.2f}, {y1:3.2f}) --> ({x2:3.2f}, {y2:3.2f})")
    print(f"Die Buttons, die Sie verwendet haben, waren: {eclick.button} {erelease.button}")
```
