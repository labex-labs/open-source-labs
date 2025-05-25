# Atualizar o Texto do Rótulo no Movimento do Mouse

Atualizaremos o texto do rótulo para exibir as coordenadas x,y do mouse quando ele for arrastado sobre o eixo. Criamos uma função para atualizar o texto do rótulo e a conectamos ao `motion_notify_event` usando o método `mpl_connect()`.

```python
def update(event):
    if event.xdata is None:
        label.set_markup('Drag mouse over axes for position')
    else:
        label.set_markup(
            f'<span color="#ef0000">x,y=({event.xdata}, {event.ydata})</span>')

fig.canvas.mpl_connect('motion_notify_event', update)
```
