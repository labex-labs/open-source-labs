# Definir la función de devolución de llamada de selección

La función de devolución de llamada de selección se llamará cada vez que el usuario seleccione un rectángulo o una elipse. La función recibirá los eventos de clic y liberación como argumentos y mostrará las coordenadas del rectángulo o la elipse.

```python
def select_callback(eclick, erelease):
    """
    Callback for line selection.

    *eclick* and *erelease* are the press and release events.
    """
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    print(f"({x1:3.2f}, {y1:3.2f}) --> ({x2:3.2f}, {y2:3.2f})")
    print(f"The buttons you used were: {eclick.button} {erelease.button}")
```
