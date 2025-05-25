# Desenhar Sombras

Desenhamos sombras para as linhas usando as mesmas linhas com um ligeiro deslocamento e cores cinza. Ajustamos a cor e a `zorder` das linhas de sombra para que sejam desenhadas abaixo das linhas originais. Também usamos o método `offset_copy()` para criar uma transformação de deslocamento para as linhas de sombra.

```python
for l in [l1, l2]:
    xx = l.get_xdata()
    yy = l.get_ydata()
    shadow, = ax.plot(xx, yy)
    shadow.update_from(l)

    shadow.set_color("0.2")
    shadow.set_zorder(l.get_zorder() - 0.5)

    transform = mtransforms.offset_copy(l.get_transform(), fig1, x=4.0, y=-6.0, units='points')
    shadow.set_transform(transform)

    shadow.set_gid(l.get_label() + "_shadow")
```
