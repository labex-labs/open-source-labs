# Mausbewegungsevent

Wir können uns an Mausbewegungsevents über die Methode `motion_notify_event` anmelden. In diesem Beispiel werden die x- und y-Koordinaten der Daten sowie die x- und y-Koordinaten der Pixel ausgegeben, wenn die Maus über dem Plot bewegt wird.

```python
def on_move(event):
    if event.inaxes:
        print(f'data coords {event.xdata} {event.ydata},',
              f'pixel coords {event.x} {event.y}')

binding_id = plt.connect('motion_notify_event', on_move)
```
