# Definir función de devolución de llamada

Necesitamos definir una función de devolución de llamada para los botones de verificación. Esta función se llamará cada vez que se haga clic en un botón de verificación. Utilizaremos esta función para alternar la visibilidad de la línea correspondiente en el gráfico.

```python
def callback(label):
    ln = lines_by_label[label]
    ln.set_visible(not ln.get_visible())
    ln.figure.canvas.draw_idle()

check.on_clicked(callback)
```
