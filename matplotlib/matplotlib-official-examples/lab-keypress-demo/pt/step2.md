# Definir a Função do Evento de Pressionamento de Tecla

Em seguida, definimos uma função `on_press` que será chamada quando uma tecla for pressionada. Esta função recebe um parâmetro `event` que contém informações sobre a tecla que foi pressionada. Neste exemplo, alternaremos a visibilidade do rótulo do eixo x (x-label) quando a tecla 'x' for pressionada.

```python
def on_press(event):
    print('press', event.key)
    sys.stdout.flush()
    if event.key == 'x':
        visible = xl.get_visible()
        xl.set_visible(not visible)
        fig.canvas.draw()
```
