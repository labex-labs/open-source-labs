# Créer l'animation du jeu

Maintenant que nous avons défini la classe `Game`, nous pouvons créer l'animation du jeu en instanciant un objet `Game` et en appelant sa méthode `draw()` dans une boucle.

```python
fig, ax = plt.subplots()
canvas = ax.figure.canvas
animation = Game(ax)

# désactiver les liaisons de touches par défaut
if fig.canvas.manager.key_press_handler_id is not None:
    canvas.mpl_disconnect(fig.canvas.manager.key_press_handler_id)


# réinitialiser l'arrière-plan de la copie mémoire lors du redessin
def on_redraw(event):
    animation.background = None


# amorcer après le premier dessin
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
