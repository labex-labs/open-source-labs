# Definir a Função de Evento 'On Pick'

Definiremos a função de evento 'on pick' que alternará a visibilidade da linha original correspondente à linha proxy da legenda.

```python
def on_pick(event):
    # On the pick event, find the original line corresponding to the legend
    # proxy line, and toggle its visibility.
    legline = event.artist
    origline = lined[legline]
    visible = not origline.get_visible()
    origline.set_visible(visible)
    # Change the alpha on the line in the legend, so we can see what lines
    # have been toggled.
    legline.set_alpha(1.0 if visible else 0.2)
    fig.canvas.draw()
```
