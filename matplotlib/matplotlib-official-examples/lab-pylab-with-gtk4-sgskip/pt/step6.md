# Atualizar o rótulo com as coordenadas do cursor

```python
def update(event):
    if event.xdata is None:
        label.set_markup('Drag mouse over axes for position')
    else:
        label.set_markup(
            f'<span color="#ef0000">x,y=({event.xdata}, {event.ydata})</span>')

fig.canvas.mpl_connect('motion_notify_event', update)
```

Criamos uma função que atualiza o rótulo com as coordenadas x e y do cursor quando ele se move sobre os gráficos. Conectamos a função ao `motion_notify_event` do canvas.
