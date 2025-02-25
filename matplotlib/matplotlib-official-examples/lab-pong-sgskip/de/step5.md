# Erstelle die Spielanimation

Jetzt, nachdem wir die `Game`-Klasse definiert haben, können wir die Spielanimation erstellen, indem wir ein `Game`-Objekt instanziieren und in einer Schleife seine `draw()`-Methode aufrufen.

```python
fig, ax = plt.subplots()
canvas = ax.figure.canvas
animation = Game(ax)

# deaktiviere die standardmäßigen Tastatureingaben
if fig.canvas.manager.key_press_handler_id is not None:
    canvas.mpl_disconnect(fig.canvas.manager.key_press_handler_id)


# Setze den Blitting-Hintergrund beim Neuziehen zurück
def on_redraw(event):
    animation.background = None


# Starte die Animation nach der ersten Zeichnung
def start_anim(event):
    canvas.mpl_disconnect(start_anim.cid)

    start_anim.timer.add_callback(animation.draw)
    start_anim.timer.start()
    canvas.mpl_connect('draw_event', on_redraw)


start_anim.cid = canvas.mpl_connect('draw_event', start_anim)
start_anim.timer = animation.canvas.new_timer(interval=1)

tstart = time.time()

plt.show()
print('FPS: %f' % (animation.cnt/(time.time() - tstart)))
```
