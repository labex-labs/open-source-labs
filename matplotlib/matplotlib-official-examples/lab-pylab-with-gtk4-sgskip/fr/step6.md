# Mettez à jour l'étiquette avec les coordonnées du curseur

```python
def update(event):
    if event.xdata is None:
        label.set_markup('Drag mouse over axes for position')
    else:
        label.set_markup(
            f'<span color="#ef0000">x,y=({event.xdata}, {event.ydata})</span>')

fig.canvas.mpl_connect('motion_notify_event', update)
```

Nous créons une fonction qui met à jour l'étiquette avec les coordonnées x et y du curseur lorsqu'il se déplace sur les tracés. Nous connectons la fonction à l'événement `motion_notify_event` de la toile.
