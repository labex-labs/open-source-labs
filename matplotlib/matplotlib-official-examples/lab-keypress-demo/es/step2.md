# Definir la función de evento de pulsación de tecla

A continuación, definimos una función `on_press` que se llamará cuando se presione una tecla. Esta función toma un parámetro `event` que contiene información sobre la tecla que se presionó. En este ejemplo, cambiaremos la visibilidad de la etiqueta del eje x cuando se presione la tecla 'x'.

```python
def on_press(event):
    print('presionar', event.key)
    sys.stdout.flush()
    if event.key == 'x':
        visible = xl.get_visible()
        xl.set_visible(not visible)
        fig.canvas.draw()
```
