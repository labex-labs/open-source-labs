# Criar a Animação do Jogo

Agora que temos a classe `Game` definida, podemos criar a animação do jogo instanciando um objeto `Game` e chamando seu método `draw()` em um loop.

```python
fig, ax = plt.subplots()
canvas = ax.figure.canvas
animation = Game(ax)

# desabilitar as ligações de teclas padrão
if fig.canvas.manager.key_press_handler_id is not None:
    canvas.mpl_disconnect(fig.canvas.manager.key_press_handler_id)


# reiniciar o fundo de blitting ao redesenhar
def on_redraw(event):
    animation.background = None


# bootstrap após o primeiro desenho
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
