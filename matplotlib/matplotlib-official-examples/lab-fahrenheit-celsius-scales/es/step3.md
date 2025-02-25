# Definir una función para actualizar el segundo eje

Definiremos una función de clausura para registrarse como una devolución de llamada para actualizar el segundo eje según el primer eje.

```python
def convert_ax_c_to_celsius(ax_f):
    """
    Actualiza el segundo eje según el primer eje.
    """
    y1, y2 = ax_f.get_ylim()
    ax_c.set_ylim(fahrenheit2celsius(y1), fahrenheit2celsius(y2))
    ax_c.figure.canvas.draw()
```
