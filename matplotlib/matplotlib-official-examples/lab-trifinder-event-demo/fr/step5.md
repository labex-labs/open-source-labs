# Configurer l'interactivité

Nous devons configurer l'interactivité pour mettre à jour le triangle sous le curseur. Nous utiliserons l'événement `motion_notify_event` pour détecter lorsque la souris est déplacée sur la représentation graphique. Nous créerons une fonction `on_mouse_move()` qui obtiendra le triangle sous le curseur en utilisant l'objet TriFinder, mettra à jour le polygone avec les sommets du triangle et mettra à jour le titre de la représentation graphique avec l'index du triangle.

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
