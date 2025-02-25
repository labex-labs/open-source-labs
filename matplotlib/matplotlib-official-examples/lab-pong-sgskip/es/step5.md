# Crear la animación del juego

Ahora que tenemos definida la clase `Game`, podemos crear la animación del juego instanciando un objeto `Game` y llamando a su método `draw()` en un bucle.

```python
fig, ax = plt.subplots()
canvas = ax.figure.canvas
animation = Game(ax)

# deshabilitar los enlaces de teclado predeterminados
if fig.canvas.manager.key_press_handler_id is not None:
    canvas.mpl_disconnect(fig.canvas.manager.key_press_handler_id)


# restablecer el fondo de la técnica de transferencia de bits en la redibujado
def on_redraw(event):
    animation.background = None


# iniciar después del primer dibujo
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
