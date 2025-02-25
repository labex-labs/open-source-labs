# Mettre à jour le texte de l'étiquette lors du mouvement de la souris

Nous allons mettre à jour le texte de l'étiquette pour afficher les coordonnées x,y de la souris lorsqu'elle est déplacée sur l'axe. Nous créons une fonction pour mettre à jour le texte de l'étiquette et la connectons à l'événement `motion_notify_event` en utilisant la méthode `mpl_connect()`.

```python
def update(event):
    if event.xdata is None:
        label.set_markup('Drag mouse over axes for position')
    else:
        label.set_markup(
            f'<span color="#ef0000">x,y=({event.xdata}, {event.ydata})</span>')

fig.canvas.mpl_connect('motion_notify_event', update)
```
