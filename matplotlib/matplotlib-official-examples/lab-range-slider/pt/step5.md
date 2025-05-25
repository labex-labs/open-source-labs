# Criar uma função de callback para o slider

Criaremos uma função de callback que será chamada sempre que o usuário alterar os valores do limiar usando o slider. A função atualizará o colormap da imagem e as posições das linhas verticais no histograma.

```python
def update(val):
    # The val passed to a callback by the RangeSlider will
    # be a tuple of (min, max)

    # Update the image's colormap
    im.norm.vmin = val[0]
    im.norm.vmax = val[1]

    # Update the position of the vertical lines
    lower_limit_line.set_xdata([val[0], val[0]])
    upper_limit_line.set_xdata([val[1], val[1]])

    # Redraw the figure to ensure it updates
    fig.canvas.draw_idle()


slider.on_changed(update)
```
