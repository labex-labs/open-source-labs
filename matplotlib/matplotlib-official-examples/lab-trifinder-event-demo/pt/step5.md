# Configurar a Interatividade

Precisamos configurar a interatividade para atualizar o triângulo sob o cursor. Usaremos o `motion_notify_event` para detectar quando o mouse é movido sobre o gráfico. Criaremos uma função `on_mouse_move()` que obterá o triângulo sob o cursor usando o objeto TriFinder, atualizará o polígono com os vértices do triângulo e atualizará o título do gráfico com o índice do triângulo.

```python
def on_mouse_move(event):
    if event.inaxes is None:
        tri = -1
    else:
        tri = trifinder(event.xdata, event.ydata)
    update_polygon(tri)
    ax.set_title(f'Triangle {tri}')
    event.canvas.draw()

fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)
```
