# Événement de mouvement de la souris

Nous pouvons nous connecter à des événements de mouvement de la souris en utilisant la méthode `motion_notify_event`. Dans cet exemple, nous affichons les coordonnées de données x et y et les coordonnées de pixels x et y lorsque la souris se déplace sur le tracé.

```python
def on_move(event):
    if event.inaxes:
        print(f'data coords {event.xdata} {event.ydata},',
              f'pixel coords {event.x} {event.y}')

binding_id = plt.connect('motion_notify_event', on_move)
```
